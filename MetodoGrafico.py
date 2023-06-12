#Importar las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definir las restricciones y la función objetivo
x = np.linspace(0, 20, 100)
y1 = 20 * np.ones(len(x))
y2 = 10 * np.ones(len(x))
y3 = (12 - 3 * x) / 4
z = 9000 * x + 1200 * y1

# Identificar la región factible
xf = x[x <= 20]
yf1 = y1[x <= 20]
yf2 = y2[x <= 20]
yf2 = y3[x <= 20]

# Calcular la función objetivo en los vértices de la región factible
vertices = [(0, 0), (0, 10), (20, 0), (20, 10)]
valores = [9000 * v[0] + 1200 * v[1] for v in vertices]

# Encontrar el vértice que maximiza la función objetivo
punto_optimo = vertices[valores.index(max(valores))]

# Graficar la región factible y el punto óptimo
plt.plot(x, y1, label='X <= 20')
plt.plot(x, y2, label='Y <= 10')
plt.plot(x, y3, label='3X + 4Y >= 12')
plt.fill_between(x,y3,y2, where=(x <= 20), color='red', alpha=0.3)
plt.plot(x, z, label='Z = 9000X + 1200Y')
plt.xlim((0, 25))
plt.ylim((0, 15))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Método Gráfico')
plt.legend()

# Hallar el punto óptimo y el valor óptimo de la función objetivo
x_opt = 20
y_opt = 10
z_opt = 9000*x_opt + 1200*y_opt
plt.scatter(x_opt, y_opt, color = 'r', label = 'Punto optimo ({},{})'.format(x_opt, y_opt))                 
plt.annotate('Z= {}'.format(z_opt),xy=(x_opt,y_opt), xytext=(x_opt+15,y_opt+15),
arrowprops =dict(facecolor = 'red', shrink = 0.05))
plt.legend()

print('El punto óptimo es:', punto_optimo)
print('El valor máximo de la función objetivo es:', max(valores))

# Mostrar la gráfica en una ventana emergente
plt.show()