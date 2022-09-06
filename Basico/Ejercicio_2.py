# EJERCICIO 1

"""
   Dado el siguiente listado: ["Python", "Matlab", "R", "VBA", "Julia", "C++"].
    Modifica con un algoritmo ese listado.
    Cuando encuentre Python debe poner un 1
    y cuando encuentre otro lenguaje de programacion, un 0
    es un simple ejemplo de modificación de valores en una lista.
"""



listado= ["Python", "Matlab", "R", "VBA", "Julia", "C++"]
#print(listado)

def modificado(listado):
    for i in range(len(listado)):
        if listado[i] == "Python":
            listado[i] = 1
        else:
            listado[i] = 0
    print(listado)

#modificado(listado)


# EJERCICIO 2

"""
    Dada la siguiente lista:
    L = [10, None, 8, 5, None, 20]
"""
    # 1) Susitituir por -1 el valor None usando bucles y listas
    # 2) Creamos un dataframe con los valores de la lista y
    #     modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)
    # 3) Vuelve a escribir el listado con falta de valores (inicial),
    #     y sustituye por la media.
    # 4) Apendiza la columna con estos valores
    #     listado2 = [10, 20, 50, 30, 20, 0]
    # 5) Elimina la columna L

L = [10, None, 8, 5, None, 20]
#print(L)

#1)

def sustituir(L):
    for i in range(len(L)):
        if L[i] == None:
            L[i] = -1
    print(L)
            
#sustituir(L)

#2)Creamos un dataframe con los valores de la lista y
# #  modificamos los "NaN" por un valor de -1 (Valores nulos, suma, etc..)

import pandas as pd

lista =[10, None, 8, 5, None, 20]

def test(lista):
    df=pd.DataFrame(lista, columns=["listado"])
    print(df)
test(lista)

def test2(lista):
    df=pd.DataFrame(lista, columns=["listado"])
    df= df.listado.fillna(-1)
    print(df)

test2(lista)

#3) Vuelve a escribir el listado con falta de valores (inicial) y sustituye por la media.

L = [10, None, 8, 5, None, 20]
def test3(L):
    df=pd.DataFrame(L, columns=["listado"])
    df= df.listado.fillna(df.listado.mean())
    print(df)

#test3(L)

#4) Apendiza la columna con estos valores # listado2 = [10, 20, 50, 30, 20, 0]

listado2 = [10, 20, 50, 30, 20, 0]

def test4(L):
    df=pd.DataFrame(L, columns=["listado"])
    df['listado2'] = listado2
    print(df)

#test4(L)

# 5) Elimina la columna L
def test5(L):
    df=pd.DataFrame(L, columns=["listado"])
    df=df.drop(["listado"], axis=1)
    print(df)

#test5(L)

# EJERCICIO 3

"""
    Crear un listado con los siguientes numeros:
        10, 20, 30, 40 (nombra la lista con nombre: "listado")
"""
    # 1) Crea el listado e imprimelo:
    # 2) Apendiza el valor 50 ( si es posible)
    # 3) Modifica (si es posible) el valor 10 por 100

listado=[10,20,30,40]
#1)
def lista(listado):
    print(listado)

#lista(listado)

#2) 
def lista2(listado, numero):
    listado.append(numero)
    print(listado)

#lista2(listado, 50)

#3)
def lista3(listado, numero):
    listado[0]=numero
    print(listado)

#lista3(listado, 100)

# EJERCICIO 4

"""
    Da una lista de nombre "Temperatura" con valores: 10, 20, 30, 40, 50
"""
    # 1) Crea el listado e imprimelo:
Temperatura=[10,20,30,40,50]
#print(Temperatura)

    # 2) En este "Temperatura". ¿Cuál es el elemento en la posición (index) 1?
def indexValue(Temperatura, i):
    return Temperatura[i]

#print(indexValue(Temperatura,1))
    # 3) ¿Y en la posición (index) 0?

#print(indexValue(Temperatura,0))

    # 4) ¿Y en la posición (index) -1?
#print(indexValue(Temperatura,-1))


    
