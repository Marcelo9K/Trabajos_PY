import matplotlib.pyplot as plt
import numpy as np

def aleatorio(n=20):
    import random as rd
    Value=[] #lista vacia
    for i in range (n): #incio de un bucle es con el : el identado es importante
        Value.append(rd.randint(1,30)) #append añade a la lista\
    return(Value) #lo que devuelve la funcion

ejex=[i for i in range(30)]
ejey=aleatorio(30)
ejey2=aleatorio(30)
#plt.title()
plt.scatter(ejex,ejey)      #datos en forma de dispersión
plt.plot(ejex,ejey)     #datos de ploteo (X;Y) en forma de lineas 
plt.show()      #grafica la imagen