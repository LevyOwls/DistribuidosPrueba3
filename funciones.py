import numpy.matlib
import math 
import numpy as np 

def to_readable(path,name):
	#[][]
    datos = np.loadtxt(path, delimiter=',',dtype='str')

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
    #########################SEPARADOR##################################################

    #No se normalizar
    #datos=Normalize(datos)
    #########################SEPARADOR##################################################
    #Se escribe el archivo nuevo
    np.savetxt(name, datos, delimiter=',')

#EJEMPLO DE USO
#to_readable("KDDTrain+_20Percent.txt","train.txt")
#to_readable("KDDTest+.txt","test.txt")

################################################################################################################
################################################################################################################
################################################################################################################

def Normalize(datos):
    data_normal = np.empty_like(datos)
    #x_min, x_max deben ser int, datos debe ser una matriz de int
    x_min = np.min(datos)
    x_max = np.max(datos)
    print("\n estos deberian ser los datos antes de normalizarlos", datos)
    for data in datos:    
        for i in data:
            data_normal = (datos[data][i]-x_min)/(x_max-x_min)
            print("dato normalizado:", data_normal)
    
   # normal =np.linalg.norm(data_normal)
   # print (normal)
    print("\n estos deberian ser los datos normalizados", data_normal)
    return data_normal

################################################################################################################
################################################################################################################
################################################################################################################  

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
	

################################################################################################################
################################################################################################################
################################################################################################################  
def random_w(next_nodes,current_nodes):
    r=math.sqrt(6/(next_nodes + current_nodes))
    w=np.random.uniform(next_nodes,current_nodes)*2*r-r;
    #int or float or something
    return(w)
################################################################################################################
################################################################################################################
################################################################################################################     
def activacion(x,w):
    
    z=np.abs(x-w)
    return np.cos(5*z)*np.exp(-0.5*z^2)

################################################################################################################
################################################################################################################
################################################################################################################    
def update_pesos(Xe,Ye,L,C):
    n=len(d)
    w1 =random_w(L,n)
    print(w1)
    print()
    bias =random_w(L,1)
    print(bias)
    print()
    biasMatrix =np.matlib.repmat(bias,1,n)
    print(biasMatrix)
    
    z=w1*Xe+biasMatrix
    
    H=activacion(z)
    
    yh=Ye*H
    hh=(H*np.transpose(H))+numpy.eye(L)/C
    inv=numpy.linalg.pinv(hh)
    w2=yh*inv
    return(w1, bias, w2)
