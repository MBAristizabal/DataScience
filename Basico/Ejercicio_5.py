#EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.

test=[25, 8, 32, 20, 1]
#print(test)

test2=list((25, 8, 32, 20, 1))
#print(test2)

# b) Apendiza un valor de valor 20, 32, 25, 32
test=[25, 8, 32, 20, 1]
test3=[20,32,25,32]

def apendiza(test):
    test=test+test3
    return test

#prin#t(apendiza(test))
#print(test)

def apendiza_1(test, numero):
    test.append(numero)
    return test

#print(apendiza_1(test, 32))
    

# c) Elimina el valor 8 de la lista

def elimina(test, i):
    test.remove(test[i])
    return test

#print(elimina(test, -1))


# d) Elimina los duplicados que haya en la lista test

test=[25, 8, 32, 20, 1, 20, 32, 25, 32]

def duplicados(test):

    return list(set(test))

# Descomentar para ejecutar:
test = duplicados(test)
#print(duplicados(test))

# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200

info=[25, 100, 10, 20, 5, 25, 30, 200]

test=[32,1,8,20,25]

# f) ¿Cuántos valores se repiten entre las listas?

def repetidos(info,test):
    contador=0
    for i in info:
        for j in test:
            if i==j:
                contador+=1
    return 'Hay', contador, 'elementos repetidos'
    
#print(repetidos(info, test))

# g) Muéstrame el maximo y mínimo en las dos listas

#print(max(test))
#print(max(info))
#print(min(info))
#print(min(test))

def limites(test):
    return min(test), max(test)

#print(limites(test))

# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz
from re import I
import numpy as np

matriz=np.array([32,1,20,25])
#print(matriz)

# i) Crea una función que se llame "funcion_división" donde se divida
# el test con valor 32 entre info con valor 5 y muestra el resto de la división

def funcion_división(n, s):
    return test[n] % info[s]

def posicion(valor, listado):
    n = 0
    for i in listado:
        if i == valor:
            break
        n += 1
    return n

#print(posicion(32, test))
#print(posicion(5, info))

# Descomentar para ejecutar:
#print(funcion_división(posicion(32, test), posicion(5, info)))

# j) Con ayuda de reverse() muestra la inversa de test
#print(test)
test.reverse()
#print(test)

# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"
info1=enumerate(info)
#print(info1)

#newDict=list(info)

#for k,v in enumerate(info):
    #print ('k',k,'v',v)

#print(newDict)

# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"
info=[25, 100, 10, 20, 5, 25, 30, 200]
info2=[]
def sustituir(listado):
    for i in info:
        if i==25:
            info2.append('Maria')
        if i==20:
            info2.append('Juan')
        if i==10:
            info2.append('Pedro')
        else:
            info2.append(i)
    return info2

#print(sustituir(info))

# m) Sustituye en el listado test los multiplos de 2 por "Dos"
test=[32,1,8,20,25]

def sustituir2(listado):
    for i in range (len(test)):
        if test[i]%2==0:
            test[i]='Dos'
    return test

#print(sustituir2(test))
    
# EJERCICIO 2
"""
#Escribe un programa que imprima los números desde 1 hasta 100
    #Pero:
    #* Para los múltiplos de 3 escribe "Hello"
    #* Para los múltiplos de 5 escribe "World"
    #* Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    #(en vez de los números correspondientes)
    """
listado=np.arange(0,101,1)
listado.tolist()
print(listado)
def multiplos(listado):
    for i in listado:
        if listado[i]%3 == 0 and listado[i]%5 == 0:
            listado[i] = "Hello World"
        if listado[i]%3 == 0:
            listado[i] = "Hello"
        if listado[i]%5 == 0:
            listado[i] = "World"
        else:
            listado[i]= i
    return np.array(listado)


#print(multiplos(listado))