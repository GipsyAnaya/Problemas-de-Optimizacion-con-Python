#Importar librerias necesarias
from pulp import *

#Crear el problema de minimización
problema = LpProblem("Problema de optimización", LpMinimize)

#Definir las variables de decisión
x1 = LpVariable("x1", lowBound=0)
x2 = LpVariable("x2", lowBound=0)

#Definir la función objetivo
problema += 6*x1 + 2*x2

#Definir las restricciones
restriccion1 = 0.5*x1 + 0.2*x2 <= 4
restriccion2 = 2*x1 + 3*x2 >= 20
restriccion3 = 1*x1 + 1*x2 == 10

problema += restriccion1
problema += restriccion2
problema += restriccion3

#Resolver el problema
problema.solve()

#Imprimir el resultado
print("Estado de la solución:", LpStatus[problema.status])
print("Valor de x1=", value(x1))
print("Valor de x2=", value(x2))
print("Valor Óptimo de la función objetivo Z=", value(problema.objective))
