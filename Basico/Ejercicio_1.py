#EJERCICIO

"""Describe  una variable con nombre "notas" que muestre el valor -3"""
#mostrar su valor 
notas= -3
print(notas)


#EJERCICIO2

"""
Imprime los valores de "s" es igual a 25, de "y" es igual a 10, poniendo la siguiente salida:"""
"""El valor de "s" es "valor de s" y el valor de "y" es "valor de y"
"""
s = 25
y = 10
print(f'el valor de s es {s} y el valor de y es {y}')
print('el valor de s es ' +str(s) + 'el valor de y es' + str(y))
print('el valor de s es ', s, 'el valor de y es ',y)
print(f'el valor de s es %s y el valor de y es %s' %(s,y))


#EJERCICIO 3

"""
Declarar una variable con nombre "name" que contenga el valor de Juan "El Profesor"
"""
name = "Juan 'El Profesor'"
name 



# EJERCICIO 4

"""
    Concatena las siguientes palabras formando un sola:
    Juan "El profesor"
"""
name= " Juan" + " " + " El Profesor"
name

# EJERCICIO 5

"""
    Teniendo la siguientes palabras: no cuentes los días, haz que los días cuenten
     · Pon las primeras letras de cada palabra en mayúsculas
     · Pon todas las letras en mayúsculas
     · Pon todas las letras en minúculas
"""

frase= "No cuentes los dias, haz que los dias cuenten"

frase = frase.title()
frase

frase = frase.upper()
frase

frase = frase.lower()
frase



# EJERCICIO 6

"""
    Realiza la suma de 26 y 35
    Realiza la multiplicación de 26 y 35
    Realiza la operación de 2 + 32 por 10
    Saca el resultado de 3 elevado a 9
    Redondea el resultado anterior a dos decimales
    Muestra de que tipo se trata
"""

suma = 26 + 35
suma

multi= 26 * 35
multi

operacion = (2+32)*10
operacion 

elevado = 3**9
elevado

redondea = round(elevado, 2)
redondea

type(redondea)

# EJERCICIO 7

"""
    Saca el valor absoluto de -32
    Muestra el máximo y el mínimo de (3, -6, 4, -10, 2.6666)
"""

absoluto = abs(-32)
absoluto

listado = [3,-6,4,-10, 2.6666]
listado

min(listado)

max(listado)




# EJERCICIO 8

"""
    Tratar de reemplazar los valores que faltan en este listado --> por un -1
    L = [10, None, 8, 5, None, 20]
    1) Hazlo de la forma más fácil posible teniendo en cuenta la posición (index) de esos valores.
    2) Crea un dataframe con esos valores (L = [10, None, 8, 5, None, 20])
"""
L = [10, None, 8, 5, None, 20]

L[1]= -1
L[-2]= -1

L
