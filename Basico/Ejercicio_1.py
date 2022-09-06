#EJERCICIO 1

"""Describe  una variable con nombre "notas" que muestre el valor -3"""
#mostrar su valor 
notas= -3
#print(notas)


#EJERCICIO2

"""
Imprime los valores de "s" es igual a 25, de "y" es igual a 10, poniendo la siguiente salida:"""
"""El valor de "s" es "valor de s" y el valor de "y" es "valor de y"
"""
s = 25
y = 10
#print(f'el valor de s es {s} y el valor de y es {y}')
#print('el valor de s es ' +str(s) + 'el valor de y es' + str(y))
#print('el valor de s es ', s, 'el valor de y es ',y)
#print(f'el valor de s es %s y el valor de y es %s' %(s,y))


#EJERCICIO 3

"""
Declarar una variable con nombre "name" que contenga el valor de Juan "El Profesor"
"""
name_1 = "Juan 'El Profesor'"
 
def profesor_1(name_1):
    return name_1
#print(profesor_1(name_1))

# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""

def profesor_2(name_1, name_2):
    result = name_1 + " " + name_2
    print(result)

# profesor_2("Juan", "'El profesor'")

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

frase= "No cuentes los dias, haz que los dias cuenten"
def mayuscula(frase):
    return frase.title()

#print(mayuscula(frase))

def mayuscula_todas(frase):
    return frase.upper()
#print(mayuscula_todas(frase))

def minuscula_todas(frase):
    return frase.lower()
#print(minuscula_todas(frase))

# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""

def suma(x,y):
    suma= x + y
    return suma
#print(suma(26,35))

def multi(x,y):
    producto= x * y
    return producto
#print(multi(26,35))

def operacion(x,y,z):
    operar = (x + y)*z
    return operar
#print(operacion(26,35,10))

def elevar(x,y):
    eleva = (x **y)
    return eleva
#print(elevar(3,9))

def redondeo(value):
    print(round(value, 2))

#redondeo(19.3333)

def tipo(value):
    print(type(value))

#tipo(19.333)


# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""

def absoluto(value):
    print(abs(value))

#absoluto(-32)

listado = [3,-6,4,-10, 2.6666]
def minimo(listado):
    minimo=min(listado)
    return minimo
#print(min(listado))

def maximo(listado):
    maximo=max(listado)
    return maximo
#print(max(listado))


# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""
L = [10, None, 8, 5, None, 20]
def test(L):
    L[1]=-1
    L[-2]=-1
    return L
#print(test(L))

import pandas as pd
def test1(L):
    df= pd. DataFrame(L, columns=["listado"])
    return df
#print(test1(L))