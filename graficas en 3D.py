# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:09:10 2020

@author: ferna
"""
"""Se analizó gráficamente el siguiente sistemas de ecuaciones 3x3:
    2x+4y+6z=22
    3x+8y+5z=27
    -x+y+2z=2
    """
    
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D #Para ver los ejes en 3D
from matplotlib import cm #Para los mapas en colores

A = np.array([[2,4,6],[3,8,5],[-1,1,2]])
b = np.array([22,27,2]) #Vector solución 
c = np.linalg.solve(A,b) 
print(c)

x,y = np.linspace(0,10,10),np.linspace(0,10,10) #Ecuaciones para graficarlas (valores de 'x' y 'y')
X,Y = np.meshgrid(x,y) #Crear la cuadricula

#Despeje de las ecuaciones para "Z"
Z1 = (22-2*X-4*Y)/6
Z2 = (27-4*X-8*Y)/5
Z3 = (2+X-Y)/2

fig = plt.figure() 
ax = fig.add_subplot(111,projection="3d") #Nombre del gráfica en el programa
ax.plot_surface(X,Y,Z1,alpha=0.5,cmap=cm.flag,rstride=100,cstride=100) #Tipo de gráfica, superficie 
ax.plot_surface(X,Y,Z2,alpha=0.5,cmap=cm.Pastel1,rstride=100,cstride=100)
ax.plot_surface(X,Y,Z3,alpha=0.5,cmap=cm.Paired,rstride=100,cstride=100)
#Alpha es la trasnparencia que tendrá, rstride es el espacio que hay entre los valores

#Para marcar la solución
ax.plot((c[0],),(c[1],),(c[2],),lw=2,c='k',marker='o',markersize=7,markeredgecolor='g',markerfacecolor='white')

#nombres a los ejes
ax.set_xlabel("Potencia");ax.set_ylabel("Corriente");ax.set_zlabel("Resistencia")
plt.show() 