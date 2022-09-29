import pandas as pd

# EJERCICIO 1 

# Calcula la longitud de una cadena de texto sin usar la instruccion len(cadena)

# 1) Cadena de texto: hola como estas?

    # Nombre de la variable: "cadena"



cadena='hola como estas?'
def cuenta(cadena):
    contador=0
    for letra in cadena:   
        contador +=1
        return contador

#print(cuenta(cadena))        

# 2) Longitud de la cadena de texto
len(cadena)
#print(len(cadena))

# 3) Longitud de la cadena de texto calculada con un bucle
cuenta=0
for letra in cadena:
    cuenta +=1
#print("la longitud es:" , cuenta)


# EJERCICIO 2

# Crea un diccionario que tenga la nota de 3 asignaturas y

# haz un pequeño algoritmo que calcule la nota media

# CURSO         -> Nota
# ---------------------
# Python        ->  10
# Big Data      ->  8
# NLP           ->  6
curso=["Python", "Big Data", "NLP"]
nota=[10,8,6]
diccionario=(dict(zip(curso,nota)))
#print(diccionario)

# 1) Muestra el valor de las claves
#print(diccionario.keys())

# 2) Muestra el valor de los valores del diccionario
#print(diccionario.values())

# 3) Apendiza en el diccionario un nuevo elemento:

    # Machine Learning --> 9

diccionario["Machine Learning"]=9

#print(diccionario)

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.

    # [["clave1", valor1], ["clave2", valor2]]

def anidada(diccionario):
    list_main=[]
    for k, v in  diccionario.items():
        list_info=[]
        list_info.append(key)
        list_info.append(value)
        list_main.append(list_info)
    return list_main
#print(anidada(nota))
            
# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta

curso=["Python", "Big Data", "NLP", "Machine Learning"]
nota=[10,8,6,9]

df=pd.DataFrame({"Asignatura": curso, "Nota": nota})
#print(df)
#print(df.max())
# 6) ¿y la nota más baja?
#print(df.min())
# 7) Ordena el dataframe en orden descendente:
#print(df.sort_values("Nota", ascending=False))


# EJERCICIO 3

"""
Dadas 2 funciones:
Determina cual de ellas ejecuta mas rápido.
Si sabes, hazlo de 2 formas.
función a
def main(): for i in range(10**8): pass
main()
función b
def main(): for i in np.arange(10**8): pass
main()
de 2 formas
"""
#inicial= time.time()
 
def main():
    for i in range (10**8):
        pass

#main()

#final= time.time()


# EJERCICIO 4
import numpy as np
# Dada:

# Una matriz tal que así:
A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python

def matriz(A):
    A=np.array([[1,2,3], [4,5,6], [7,8,9]])
    return A
    
#print(matriz(A))

# 2) Escribe la matriz transpuesta.

def transpuesta(A):
    m_transpuesta = A.T
    return m_transpuesta
#print(transpuesta(A))
    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.

def transpuesta():
    list_main=[]
    for i in range(3):
        list_row=[]
        for j in range(3):
            list_row.append(A[j][i])
        list_main.append(list_row)
    trans=np.array(list_main)
    return trans

#print(transpuesta())
