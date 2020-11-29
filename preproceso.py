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

#param: dato[][]
def Normalize(datos):
    data_normal = np.empty_like(datos)
    
    #x_min, x_max deben ser int, datos debe ser una matriz de int
    x_min = np.min(datos)
    x_max = np.max(datos)
    print("\n estos deberian ser los datos antes de normalizarlos", datos)
    for data in datos: 
        contador = 0
        for i in data:
            #aux=str(i);
            x = i.astype(float)
            data_normal[contador] = (x-x_min)/(x_max-x_min)
            contador+=1
    
   # normal =np.linalg.norm(data_normal)
   # print (normal)
    print("\n estos deberian ser los datos normalizados", data_normal)
    
    return data_normal

##############################################################
##############################################################
  

def preproceso():
    path = 'KDDTrain+_20Percent.txt'
    datos = np.loadtxt(path, delimiter=',',dtype='str')
    
   # print(datos)

    
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
            if contador == 41:
                data[contador]=transform(str(i),4)
            #Actualiza el contador
            contador+=1
    
    
    datos = datos.astype(np.float)
    datos=Normalize(datos)
    print ("\nDatos ya procesados a numero  (float)")

    #Se escribe el archivo nuevo
    np.savetxt('train.txt', datos, delimiter=',')
    