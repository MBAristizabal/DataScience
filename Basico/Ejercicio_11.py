# Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt


# EJERCICIO 1

"""
    Escribe el código necesario en Python para:
    almacenar con una lista de nombre "clientes" los siguientes nombres:
    "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"
"""
clientes=["Ana Perez", "Juan Garcia", "Andres Alvarez", "Luis Ramos", "Pedro Cadenas",
    "Estefania Miguelez", "Alberto Delgado", "Susana Castro", "Luis Gonzalez"]
#print(clientes)
# 1) Para ese listado de clientes imprime todos ellos, 1 a 1

def deauno(clientes,i):
    return clientes[i]

#print(deauno(clientes,3))

def iteracion(clientes):
    for cliente in clientes:
        print(cliente)
#iteracion(clientes)
"""
    2) Dentro de ese grupo de clientes..
    se pide buscar..al cliente de nombre: "Juan García" si es posible
    Si lo encuentra, debería imprimir un mensaje tal que así:
    "el cliente -nombre del cliente- se encuentra en mi Base de Datos de Clientes"
    Si no se le encuentra, debería salir un mensaje tal que así:
    "el cliente -nombre del cliente- NO se encuentra en mi Base de Datos de Clientes"
    Nota: Comprueba en el caso de llevar o no acento
    Para:
    Juan García
    Juan Garcia
    Ojo con la tilde..
"""

buscado= 'Alberto delgado'
#print(clientes)
def busqueda(clientes, buscado):
    for cliente in clientes:
        clientes=cliente.lower()
        buscado=buscado.lower()
    
        if buscado in clientes:
            return "El cliente",buscado, "se encuentra en nuestra Base de Clientes"
        else:
            return "El cliente",buscado, "No se encuentra en nuestra Base de Clientes"

#print(busqueda(clientes,buscado))

"""
    3) Crea un DataFrame, de nombre df
    con esa información en base a la siguiente relación de clientes y tarifas contratadas (€)
    clientes: Ana Pérez, Juan García, Andrés Álvarez, Luis Ramos, Pedro Cadenas,
            Estefanía Miguélez, Alberto Delgado, Susana Castro, Luis González
    tarifas: 40,50,50,35,45,50,60,50,45

"""
clientes=['Ana Perez', 'Juan Garcia', 'Andres Alvarez', 'Luis Ramos', 'Pedro Cadenas',
            'Estefanía Miguélez', 'Alberto Delgado', 'Susana Castro', 'Luis Gonzalez']
tarifas=[40,50,50,35,45,50,60,50,45]

df= pd.DataFrame({"Clientes":clientes, "Tarifas": tarifas})
#print(df)
# 4) Imprime las primeras 5 filas del DataFrame de 2 formas distintas
#print(df.head())

#print(df.head(5))
# 5) De ese DataFrame, selecciona solamente la columna "tarifas" e imprímela
    # (con 1 forma es suficiente, pero si sabes 2 mejor)
#print(df['Tarifas'])  
#print(df.Tarifas)  

# 6) Descomenta las siguientes líneas (algunos trucos y cosas útiles).
    # Ponlo en formato función!!

# df.tarifas.value_counts()

# df.tarifas.value_counts().plot(kind="bar")
# plt.show()

# df.tarifas.plot(kind="bar")
# plt.show

# print(df)

# 7) De ese DataFrame, selecciona solamente aquellos clientes con tarifa superior a 50 euros (50 no incluído)
#print(df[df['Tarifas']>50])

# EJERCICIO 2

# Número par o impar

# Prueba para los números 6 y 3

# Realiza un algortimo para saber si son pares o impares

def pi(numero):
    if numero%2==0:
        return f'El numero es par'
    else:
        return f'El numero es impar'

print(pi(9))

# EJERCICIO 3

"""
    Intercambio de valores entre variables
    Siendo por ejemplo:
    x = 3 e y = 2
    Se pide hacer un pequeño algoritmo que me intercambie esos valores.
    Y que sea el resultado:
    x = 2 e y = 3
"""

# 1) Hazlo sin funciones

# 2) Hazlo mismo con una función

x, y = 3, 2

# print(x, y)
aux = x

x = y

y = aux

# print(x, y)

# 2) Hazlo mismo con una función

def intercambio(x, y):
    aux = x
    x = y
    y = aux
    return x, y

x, y = intercambio(3, 2)

# print(x, y)