#EJERCICIO 1

# a) Declara la variable "test" como una lista con los siguientes componentes: 25, 8, 32, 20, 1.
    # Usa las formas que conozcas para crearla y el uso de type para asegurarte de que es una lista.

test=[25, 8, 32, 20, 1]
#print(test)

test2=list((25, 8, 32, 20, 1))
#print(test2)

# b) Apendiza un valor de valor 20, 32, 25, 32
test=[25, 8, 32, 20, 1]

def apendiza(test):
    test3=[20,32,25,32]
    test.append(test3)
    return test

print(apendiza(test))

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

#test3=[20,32,25,32]
def duplicados(test3):
   unicos=[]
   while len(unicos)<len(test3):
    unicos.append(test3[i])
    i -= 1


    #test3.set(test3)
    #return test3

#print(duplicados(test3))

#



# e) Crea una segunda lista de nombre "info" que contenga los valores:
    #  25, 100, 10, 20, 5, 25, 30, 200
"""info=[25, 100, 10, 20, 5, 25, 30, 200]
test3=[20,32,25,32]

# f) ¿Cuántos valores se repiten entre las listas?
#def repetidos(info,test):
   



# g) Muéstrame el maximo y mínimo en las dos listas



# h) Crea una nueva variable de nombre "matriz" transformando la lista test en matriz



# i) Crea una función que se llame "funcion_división" donde se divida
    # el test con valor 32 entre info con valor 5 y muestra el resto de la división



# j) Con ayuda de reverse() muestra la inversa de test


# k) Con el listado info utiliza un bucle for con la ayuda de enumerate(),
    # para mostrar posición y valor y crea un diccionario de nombre "newDict"


# l) Crea un nuevo listado con nombre "info2" donde los valores: 25 se sustituya por "María",
    # el valor 20 por "Juan" y el valor 10 por "Pedro"


# m) Sustituye en el listado test los multiplos de 2 por "Dos"



# EJERCICIO 2

"""
    Escribe un programa que imprima los números desde 1 hasta 100
    Pero:
    * Para los múltiplos de 3 escribe "Hello"
    * Para los múltiplos de 5 escribe "World"
    * Para los múltiplos de ambos (3 y 5) escribe "Hello World"
    (en vez de los números correspondientes)
"""