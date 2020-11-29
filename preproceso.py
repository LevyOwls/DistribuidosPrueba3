import numpy as np

##Cambio de datos
##Data[1]
data1 = ['tcp', 'udp', 'icmp']  
data2 = ['ftp_data', 'other', 'private', 'http', 'remote_job', 'name', 'netbios_ns', 'eco_i', 'mtp', 'telnet', 'finger', 'domain_u', 'supdup', 'uucp_path', 'Z39_50', 'smtp', 'csnet_ns', 'uucp', 'netbios_dgm', 'urp_i', 'auth', 'domain', 'ftp', 'bgp', 'ldap', 'ecr_i', 'gopher', 'vmnet', 'systat', 'http_443', 'efs', 'whois', 'imap4', 'iso_tsap', 'echo', 'klogin', 'link', 'sunrpc', 'login', 'kshell', 'sql_net', 'time', 'hostnames', 'exec', 'ntp_u', 'discard', 'nntp', 'courier', 'ctf', 'ssh', 'daytime', 'shell', 'netstat', 'pop_3', 'nnsp', 'IRC', 'pop_2', 'printer', 'tim_i', 'pm_dump', 'red_i', 'netbios_ssn', 'rje', 'X11', 'urh_i', 'http_8001']
data3 = ['SF', 'S0', 'REJ', 'RSTR', 'SH', 'RSTO', 'S1', 'RSTOS0', 'S3', 'S2', 'OTH']
data41 = ['normal', 'neptune', 'warezclient', 'ipsweep', 'portsweep', 'teardrop', 'nmap', 'satan', 'smurf', 'pod', 'back', 'guess_passwd', 'ftp_write', 'multihop', 'rootkit', 'buffer_overflow', 'imap', 'warezmaster', 'phf', 'land', 'loadmodule', 'spy']

def transform (data,lista):
    contador=0
    if lista == 1:    
        for i in data1:
            if str(i) == data:
                return contador+1
            contador+=1
    if lista == 2:
        for i in data2:
            if str(i) == data:
                return contador+1
            contador+=1
    if lista == 3:
        for i in data3:
            if str(i) == data:
                return contador+1
            contador+=1
    if lista == 4:
        if str(data) != 'normal':
            return -1
        return 1

##############################################################
##############################################################

def load_config():
	config = np.genfromtxt("configuracion.csv", dtype=float, delimiter='\n') 
	#VECTOR[ ]
	nc=1
	#Nodos ocultos
	L=config[0]
	#Particulas
	particulas=config[1]
	#Maximo de iteraciones
	max_iteraciones=config[2]
	#Penalidad P inversa
	C=config[3]
	return (nc,L,particulas,max_iteraciones,C)
	

##############################################################
##############################################################

#param: dato[][]
def Normalize_Xe(datos):
    y = np.empty_like(datos)
    
    #x_min, x_max deben ser int, datos debe ser una matriz de int
    x_min = np.min(datos)
    x_max = np.max(datos)
    print("\n estos deberian ser los datos antes de normalizarlos", datos)
    for data in datos: 
        contador = 0
        for i in data:
            #aux=str(i);
            x = i.astype(float)
            y[contador] = (x-x_min)/(x_max-x_min)
            #y=(0.99-0.1)*y+0.1
            contador+=1
    
   # normal =np.linalg.norm(data_normal)
   # print (normal)
    print("\n estos deberian ser los datos normalizados", y)
    
    return y



##############################################################
##############################################################  

def to_readable(path,name):
    datos = np.loadtxt(path, delimiter=',',dtype='str',usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40))

    #Se transforma todo a numeros enteros.
    for data in datos:
        contador=0
        for i in data:
            if contador == 1:
                data[contador]=transform(str(i),1)
            if contador == 2:
                data[contador]=transform(str(i),2)
            if contador == 3:
                data[contador]=transform(str(i),3)
            contador+=1
    datos = datos.astype(np.float)
    datos=Normalize_Xe(datos)
    #Se escribe el archivo nuevo
    np.savetxt(name, datos, delimiter=',')
    
    Y=np.loadtxt(path, delimiter=',',dtype='str',usecols=41)
    Yee=[]
    for data in Y:
        if data != 'normal':
            Yee.append(-1)
        else:
            Yee.append(1)
    Ye=np.array(Yee)
    return Ye

##############################################################
############################################################## 

def preproceso():
    Ye=to_readable("KDDTrain+_20Percent.txt","train.txt")
    Xe=np.loadtxt("train.txt", delimiter=',',dtype='float', usecols=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40))
    (nc,L,particulas,max_iteraciones,C)=load_config()
    print (Ye)
    print (Xe)
    
    
    