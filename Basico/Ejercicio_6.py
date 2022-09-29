#EJERCICIO 1

# Mínimo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40


listado=[30, 20, 10, 50, 40]

# 1) Escribe el listado e ímprimelo
#print(listado)

# 2) Prueba con min(listado)

def minimo(listado):
    min(listado)
    return(listado)
#print(minimo(listado))

# 3) Realiza lo mismo pero con bucles y condicionales
def minimo_2(lista):
    minimo = max(lista) + 1

    for numero in lista:
        if numero < minimo:
            minimo = numero

    return minimo

# print(minimo_2(listado))
  

# EJERCICIO 2

# Máximo de una lista de números (lista de nombre "listado"): 30, 20, 10, 50, 40

listado2=[30, 20, 10, 50, 40]

# 1) Escribe el listado e ímprimelo

#print(listado2)
# 2) Prueba con max(listado)
def maximo(listado2):
    return max(listado2)

#print(maximo(listado2))

# 3) Realiza lo mismo pero con bucles y condicionales

def maximo_1(lista):
    maximo = -100000000

    for numero in listado:
        if numero > maximo:
            maximo = numero
    return maximo

#print(listado)


# EJERCICIO 3

# Ordena de menor a mayor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")
listado= [30, 20, 10, 50, 40] 

# Pista: si quieres almacena esos números en una lista de nombre: "listado_ascendente"
listado_ascendente=[]

def ascendente(listado):
    while len(listado)>0:
        listado_ascendente.append(min(listado))
        listado.remove(min(listado))
    return listado_ascendente

#print(ascendente(listado))
# 1) Escribe el listado e ímprimelo

#print(listado_ascendente)
#print(listado)

# 2) Prueba a usar sort()
#listado.sort()

#print(listado)

# 3) Realiza lo mismo pero con bucles y condicionales
listado2=[30, 20, 10, 50, 40]
ordenado=[]
i=len(listado2)
def ordenar(listado2):
    while i in range(len(listado2)):
        ordenado.append(min(listado2[i]))
        listado2.remove(min(listado2[i]))
        return listado2
#print(ordenar(ordenado))


# EJERCICIO 4

# Ordena de mayor a menor un listado de números: 30, 20, 10, 50, 40 (de nombre "listado")

# 1) Escribe el listado e ímprimelo

listado= [30, 20, 10, 50, 40] 
#print(listado)
# 2) Prueba a usar sort()

listado.sort(reverse=True)
#print(listado)
# 3) Realiza lo mismo pero con bucles y condicionales



# EJERCICIO 5
"""
    Escribe el código necesario en Python para:
    * almacenar con una lista de nombre "módulos" las siguientes materias de un programa de Ciencia de Datos:
    * Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP.
"""
# 1) Para ese listado imprime todas ellas, 1 a 1
modulos = ["Big Data", "Python", "Algoritmos", "Machine Learning", "Deep Learning", "NLP"]
#print(modulos)

def deauno(modulos,i):
    return modulos[i]

#print(deauno(modulos,1))

def iteracion(modulos):
    for i in modulos:
        print(i)

#iteracion(modulos)

"""
    2) dentro de ese grupo de materias, existen unas materias que son básicas en todos los programas.
    y que forman la base de conocimientos iniciales para afrontar con éxito el resto de un programa.
    Las mismas son: Python y Algoritmos (aunque en la práctica hay más cosas)
    Se pide almacenar las mismas en un listado secundario, de nombre: "esenciales" (por ejemplo)
    Imprime ese listado al terminar de almacenarlos.
"""
esenciales=[]

def esencial(esenciales):
    for materia in modulos:
        modulos==("Python") or modulos==("Algoritmos")
        esenciales.append("Python")
        esenciales.append("Algoritmos")
        return esenciales
#print(esencial(esenciales))
"""
    3) Crea un DataFrame, de nombre df con esa información en base
    a la siguiente relación de módulos y horas de clase módulos:
    Big Data, Python, Algoritmos, Machine Learning, Deep Learning, NLP
    horas: 25, 15, 5, 15, 5, 10
"""

horas=[ 25, 15, 5, 15, 5, 10]

import pandas as pd

def programa(modulos, horas):
    df= pd.DataFrame({"modulos": modulos, "horas": horas})
    return df
#print(programa(modulos, horas))

# 4) De ese DataFrame, selecciona solamente la columna "horas" e imprímela
df= pd.DataFrame({"modulos": modulos, "horas": horas})
def hs(df):
    
    return df["horas"]
#print(hs(df))

# 5) Muestra el gráfico (plot) para la columna "horas"

#pip install matplotlib

# 6) De ese DataFrame, selecciona solamente aquellas materias que tienen 20 o más horas de dedicación

def horario(df):
    return df[df['horas']>=20]

#print(horario(df))



# 7) De ese DataFrame, selecciona solamente aquellas materias que tienen menos de 10 horas de dedicación

#print(df[df['horas']<10])
# 8) De ese DataFrame, selecciona solamente (si fuera posible)
    # aquellas materias que tienen mas de 26 horas de dedicación
#print(df[df['horas']>26])

# 9) Apendiza, (si puedes), una nueva columna llamada "docente" con el instructor encargado de la materia.

    # Y cuyos nombres serán: Enrique, Susana, Juan, Ana, Laura, Patricia

docente=['Enrique', 'Susana', 'Juan', 'Ana', 'Laura', 'Patricia']
df['Docente']=docente
#print(df)