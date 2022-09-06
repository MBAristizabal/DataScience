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

print(cuenta(cadena))        

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
curso=["Python", "Big Data", "NLP" ]
noota=[10,8,6]
diccionario=dict(zip('curso','notas'))
#print(diccionario)

# 1) Muestra el valor de las claves


# 2) Muestra el valor de los valores del diccionario

# 3) Apendiza en el diccionario un nuevo elemento:

    # Machine Learning --> 9

# 4) Haciendo uso un bucle muestra la clave y el valor del diccionario, cuyo resultado final sean listas anidadas.

    # [["clave1", valor1], ["clave2", valor2]]

# 5) Reconvierte el diccionario para transformarlo en un dataframe y busca la asignatura con la nota más alta

# 6) ¿y la nota más baja?

# 7) Ordena el dataframe en orden descendente:


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

# EJERCICIO 4

# Dada:

# Una matriz tal que así:

# A = np.array([[1,2,3], [4,5,6], [7,8,9]])

# se pide:

# 1) Escribe ese código en Python

# 2) Escribe la matriz transpuesta.

    # Nota, puedes usar numpy, si quieres. Si sabes más de una forma puedes usar varias.

# 3) Se pide que hagas lo mismo, pero con un bucle.
0 