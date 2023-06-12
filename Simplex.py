#Importar las bibliotecas
import numpy as np
from scipy.optimize import linprog

#Definir la función objetivo y las restricciones en forma de matrices
A = np.array([[4, 6], [20, 10]])
b = np.array([480, 1500])
c = np.array([110, 150])

#Resolver el problema utilizando el método simplex a través de la función linprog
result = linprog(-c, A_ub=A, b_ub=b, method='simplex')

#Imprimir el resultado
print("Solución Óptima:")
for i in range(len(result.x)):
    print("X{}: {:.2f}".format(i+1, result.x[i]))
print("Valor optimo de la función objetivo: {:.2f}".format(result.fun * -1))