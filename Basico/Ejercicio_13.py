import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# EJERCICIO 1

# NO HACE FALTA HACERLO EN FORMATO FUNCIÓN!

# Se pide por tanto:

# -1- Leer el archivo train.csv de Titanic dataset con pandas (carpeta src)
#df=pd.read_csv("./src/train/.csv")
#print(df)

# -2- Imprimir algunas filas de la parte de arriba y otras de la parte del final
#print(df.head())
#print(df.tail())

# -3- Imprimir algunos parámetros estadísticos
#print(df.describe())

# -4- Ver si en todas las columnas tenemos el mismo número de datos (solo verlo)
#print(df.shape, df.size)
# -5- Ver el número de hombres y mujeres que hay
#print(df.Sex_value.counts())

# -6- Hacer alguna gráfica con pandas relativa al número de hombres y mujeres que hay
#df.Sex.value_counts().plot(kind="bar")
#plt.show()


# Si quieres hacer alguna cosa más también puedes
#df.Survived.value_counts().plot(kind="bar")
#plt.show()

# EJERCICIO 2
"""
    Dadas estas matrices:
    * m1 = [[1, 10, 20], [30, 40, 50]]
    * m2 = [[60, 80, 90,]]
    * m3 = [[-2, 3, 5], [8, 6, 2]]
"""

# 1) Comprueba si todos los valores de las matrices son mayores de 0
m1 = np.array ([
    [1, 10, 20], 
    [30, 40, 50]
    ])
#print(m1)
m2 = np.array([[60, 80, 90,]])
#print(m2)
m3 = np.array([
    [-2, 3, 5],
    [8, 6, 2]
    ])
#print(m3)

#print(np.all(m1>0))
#print(np.all(m2>0))
#print(np.all(m3>0))

def alguno(matriz):
    if np.all(matriz)>0:
        return True
    else:
        return False
#print(alguno(m1))

# 2) Si en la matriz m2 se encuentra el valor 80
#print(80 in m2)

def encontrar(matriz,valor):
    return valor in matriz

#print(encontrar(m2,80))

# 3) Selecciona de m1 las dos últimas columnas
#print(m1[:,[1,2]])

# 4) Concatena la m1 con m2, cuyo nombre de la matriz resultante sea m4

m4= np.concatenate((m1,m2), axis=0)
#print(m4)
# 5) Convierte m1 y m3 en "np.matrix" asignando el nombre de matriz_1 y matriz_3, respectivamente
matriz_1= np.matrix(m1)
#print(matriz_1)
matriz_3= np.matrix(m3)
#print(matriz_3)

# 6) Realiza la resta, suma y producto de la matriz_1 y matriz_3

def suma_matrices(matriz_1, matriz_3):

    return matriz_1 + matriz_3
#print(suma_matrices(matriz_1, matriz_3))

def resta_matrices(matriz_1,matriz_3):
    return matriz_1 - matriz_3

#print(resta_matrices(matriz_1, matriz_3))
def producto_matrices(matriz_1, matriz_3):
    return matriz_1 * matriz_3.T
#print(producto_matrices(matriz_1, matriz_3))

# 7) Realiza las traza de la matriz de m4
#print(np.trace(m4))


# EJERCICIO 3

"""
    * Numeros Primos: Crear un listado de los numeros primos menores de 30
    Explicación inicial teórica
    (véase Tema_7..)
    Nota:
    si quieres apendiza el número 2,
    y a partir de ahí crea el algoritmo para apendizar los demas
    (menores de 30 en todo caso)
"""

# 1) Pide por teclado un número y di si es o no primo

#numero= int(input("ingrese un numero: "))
#primos=[]

#posibles=np.arange(2,31,1)
#for numero in posibles:
    #if (numero%2) != 0 :
        #primos.append(numero)
#print("es primo")
#print(primos)

# 2) Escribe los números primos menores de 30
def primos_2(inicio, fin):
    primos = []
    primos.append(2)

    for n in np.arange(inicio, fin, 1):
        listado_restos = []
        for i in np.arange(2, n):
            listado_restos.append(n % i)
        if 0 not in listado_restos:
            primos.append(n)
    return np.array(primos)

# Descomentar para ejecutar:
#print(primos_2(3, 30))


# 3) Numeros Primos: Crear un listado de los numeros primos menores de 200
#print(primos_2(3, 200))

# 4) Números Primos: HaHaz un listado de números primos entre 50 y 100
#print(primos_2(50, 100))

# 5) Numeros Primos: Haz un listado de los 10 primeros números primos
    # Si puedes hazlo de más de una forma, no necesario aun así
def primos2(inicio, fin):
    primos=[]
    primos.append(2)
    for n in np.arange(inicio,fin,1):
        listado_restos=[]
        for i in np.arange(2,n):
            listado_restos.append(n%i)
        if 0 not in listado_restos and len(primos)<10:
            primos.append(n)
    return np.array(primos)

#print(primos2(3,300))
