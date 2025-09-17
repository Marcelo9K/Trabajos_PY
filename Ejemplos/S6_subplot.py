import matplotlib.pyplot as plt
import numpy as np

def aleatorio(n=20):
    import random as rd
    Value=[] #lista vacia
    for i in range (n): #incio de un bucle es con el : el identado es importante
        Value.append(rd.randint(1,30)) #append añade a la lista\
    return(Value) #lo que devuelve la funcion

#ejex=[i for i in range(30)]
#ejey=aleatorio(30)
#ejey2=aleatorio(30)
ejex=[i*0.1 for i in range(100)]
ejey=np.sin(ejex)
ejey2=-np.sin(ejex)

#//////////////////////////////////////////////////////////////////

#fig,axs= plt.subplots(2,2)
#fig.suptitle("Datos por separado")
#axs[0,0].plot(ejex,ejey,'go',label="datos de tiempo de sueño")
#axs[0,0].set_title("lugar [0,0]")
#axs[0,0].set_xlabel("tiempo")
#axs[1,1].plot(ejex,ejey2,'rx',label="datos de tiempo de juego")
#axs[1,1].set_title("lugar [1,1]")

#//////////////////////////////////////////////////////////////////

#fig,axs = plt.subplots(2)
#fig.suptitle("datos por separado")
#axs[0].plot(ejex,ejey,'go',label="datos de tiempo de sueño")
#axs[0].set_title("datos de tiempo de sueño")
#axs[0].set_xlabel("tiempo")
#axs[1].plot(ejex,ejey2,'rx',label="datos de tiempo de juego")
#axs[1].set_title("datos de tiempo de juego")

#//////////////////////////////////////////////////////////////////
#Tarea de seno y arcseno

fig,axs = plt.subplots(2)
fig.suptitle("datos por separado")
axs[0].plot(ejex,ejey,'g',label="Seno")
axs[0].set_title("Seno")
axs[1].plot(ejex,ejey2,'r',label="Inversa del seno")
axs[1].set_title("Arcocoseno")


plt.show()
plt.savefig('salidapng')



