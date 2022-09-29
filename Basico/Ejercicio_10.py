#EJERCICIO 1

import numpy as np
# Crea una matriz con ayuda numpy:

# 1) Cuya matriz contenga 4 filas por 4 columnas de ceros
matriz=np.zeros((4,4))
def matriz():
    matriz=np.zeros((4,4))
    return matriz
#print(matriz())

# 2) Apartir de la matriz de ceros crea la matriz identidad
def identidad(matriz):
    for i in range (len(matriz)):
        for j in range (len(matriz)):
            if j==i:
                matriz[i][j]==1
    return matriz

#print(identidad(matriz))
# EJERCICIO 2

# Crea una matriz con ayuda numpy:

# Primera fila contenga: 3, 6, 8
# Segunda fila contenga: 20, 5, 7
# Tercera fila contenga: 10, 14, 1
m = np.array ([
            [3,6,8],
            [20,5,7],
            [10,14,1]])
def mat():
    m=np.array([
            [3,6,8],
            [20,5,7],
            [10,14,1]])
    return m
#print(mat())

# 1) Crea la transpuesta de esta matriz
def transpuesta(m):
    m_transpuesta= m.T
    return m_transpuesta

#print(transpuesta(m))

# 2) Muestra el tamaño de la matriz

def tamaño(m):
    tamaño= m.shape
    return tamaño

#print(tamaño(m))

# 3) Muestra las dimensiones


# 4) ¿La matriz tiene valores menores de 0?
def valores_menores(m):
    valores_menores=np.all(m<0)
    return valores_menores

#print(valores_menores(m))
# 5) ¿La matriz tiene algún valor mayor de 10?
def valores_mayores(m):
    valores_mayores=np.any(m>10)
    return valores_mayores
#print(valores_mayores(m))

# 6) Coge una muestra de 5 valores de esa matriz usando linespace

def muestra(m):
    muestra = np.linspace(m.min(), m.max(), 5)
    return muestra
#print(muestra(m))

# 7) La matriz contiene el valor 7

def test(m, numero):
    test= numero in m 
    return test
#print(test(m,7))

# 8) Crea una copia de esa matriz en una única dimensión
def unicad(m):
    unica= m.flatten()
    return unica
#print(unicad(m))

# 9) Crea una copia de esa matriz en una única dimensión, en este caso usando un bucle y una lista vacia
lista_final=[]

for i in range(len(m)):
    for j in range(len(m)):
        lista_final.append(m[i][j])
#print(lista_final)
m2=np.array(lista_final)
print(m2)

# 10) Realiza a esta última matriz creada con flatten la potencia de 3


print(pow(m2,3))