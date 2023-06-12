#Importar las librerias necesarias
import numpy as np
from scipy.optimize import linprog

#Definir los datos del problema
oferta = [15, 25, 10]
demanda = [5, 15, 15, 15]
costos = [[10, 2, 20, 11],
          [7, 9, 24, 18],
          [4, 14, 16, 18]]

#Convertir el problema de transporte en un problema de minimización
c = np.array(costos).flatten()

#Definir las restricciones de oferta y demanda
A_eq = []
b_eq = []

#Restricciones de oferta
for i in range(len(oferta)):
    restriccion = [0] * len(c)
    for j in range(len(demanda)):
        restriccion[i * len(demanda) + j] = 1
    A_eq.append(restriccion)
    b_eq.append(oferta[i])

#Restricciones de demanda
for j in range(len(demanda)):
    restriccion = [0] * len(c)
    for i in range(len(oferta)):
        restriccion[i * len(demanda) + j] = 1
    A_eq.append(restriccion)
    b_eq.append(demanda[j])

#Resolver el problema utilizando linprog
resultado = linprog(c, A_eq=A_eq, b_eq=b_eq)

# Crear la matriz de asignación a partir de las variables óptimas
asignacion = np.zeros((len(oferta), len(demanda)))
for i in range(len(oferta)):
    for j in range(len(demanda)):
        cantidad = resultado.x[i * len(demanda) + j]
        asignacion[i][j] = cantidad

#Calcular el costo total de transporte
costo_total = sum(sum(asignacion * np.array(costos)))

#Imprimir la solución
if resultado.success:
    print(f"El costo total de transporte mínimo es: {costo_total}")
    for i in range(len(oferta)):
        for j in range(len(demanda)):
            cantidad = asignacion[i][j]
            if cantidad > 0:
                print(f"Se deben transportar {cantidad} camiones cargados desde Silo {i + 1} hasta Molino {j + 1}.")
else:
    print("El problema no tiene solución óptima.")