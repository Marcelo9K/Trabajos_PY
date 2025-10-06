import numpy as np
import matplotlib.pyplot as plt


dt=[i for i in range(200)] #lista
A=[12,20] #lista
f=[0.23,0.35]
theta_i=[0.26,1.45]
x1=A[0]*np.sin(2*np.pi*f[0]*np.array(dt)*0.1+theta_i[0]) #lista
x2=A[1]*np.sin(2*np.pi*f[1]*np.array(dt)*0.1+theta_i[1]) #lista
xaco=np.array(x1)+np.array(x2)

fig,axs= plt.subplots(3,1)
fig.suptitle("Datos por separado")
axs[0].plot(x1,'g',color="#8a980dd5",label="x1")
axs[0].set_title("gráfica x1")
axs[1].plot(x2,'r',color="#0d8484d5",label="x2")
axs[1].set_title("gráfica x2")
#axs[2].plot(xaco,x1'rx',label="xaco")

plt.plot(x1)
plt.plot(x2)
plt.plot(xaco)
plt.show()