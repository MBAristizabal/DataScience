# Ejercicios
#
# *1)** Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".


#**2)** Definir un diagrama procedimiento() que tome una lista de números enteros e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

"****"

"*********"

"*******"


#**3)** Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

#**4)** Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.


#**5)** Escribir un programa que ingrese una cadenade texto. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.


#**6)** Definir una tupla con 10 edades de personas.
#* Imprimir la cantidad de personas con edades superiores a 20.



#**7)** Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)


#**8)** Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales():
    palabra=input('ingrese palabra')
    palabra=palabra.lower()
    vocales='aeiou'
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador+=1    
    return contador

    contar_vocales()
