def consultar():
    print("\n")
while True:
    print("\n")
    print("**************** MENU *******************")
    print("*****************************************")
    print("***** 1. Ejercicio 1*********************")
    print("***** 2. Ejercicio 2*********************")
    print("***** 3. Ejercicio 3*********************")
    print("***** 4. Ejercicio 4*********************")
    print("***** 5. Ejercicio 5*********************")
    print("***** 6. Ejercicio 6*********************")
    print("***** 7. Ejercicio 7*********************")
    print("***** 8. Ejercicio 8*********************")
    print("***** 9. Ejercicio 9*********************")
    print("******10.Ejercicio 10********************")
    print("***** 99.Salir (del menú) ***************")
    print("*****************************************")
    print("\n")
opcion = int(input("Inserte su opción: "))
if opcion == 1:
# ir a la funcion consultar
    consultar()
elif opcion == 99:
    
    break
else:
    print("salir del menu ")
print("\n")









# Ejercicio 1

"""
    Desarrolla el siguiente ejercicios de POO:
   * Alumnos  -> Es la clase.
   * __init__ -> Es el método init
   * nombre, edad, asignatura y nota son las propiedades
   * Instanciamos..
   * los posibles alumnos (alumno1, alumno2, alumno3..) --> son los "objetos"
   * y el.__init__ los inicializa
   A continuación muestra la edad del alumno 2 y el alumno 3 y sus notas
"""


class Alumno:

    def __init__(self, nombre, edad, asignatura, nota):
        self.nombre = nombre
        self.edad = edad
        self.asignatura = asignatura
        self.nota = nota
alumno1 = Alumno( "Juan", 17, "matematica", 7)
alumno2 = Alumno( "Jose", 17, "biologia", 6)
alumno3 = Alumno( "Lucas", 16, "quimica", 8)

alumno3.edad
alumno3.nota
alumno2.edad
alumno2.nota

# Ejercicio 2

"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def edad():
    age = int(input("¿Cuántos años tienes? "))
    for i in range(age):
        print("Has cumplido " + str(i+1) + " años")

edad()


# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""

# Ejercicio 4

"""
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces,
    una con todas las letras minúsculas,
    otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""


def nombre_completo():
    name = input("¿Cómo te llamas? ")
    print(name.lower())
    print(name.upper())
    print(name.title())

nombre_completo()
# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""



# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
frase=input('Ingrese  una frase: ')
vocal=input('Ingrese vocal: ')

if vocal in frase:
    print(vocal.upper())
    print(frase.replace(vocal,vocal.upper()))



# Ejercicio 7

"""
    Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

def precio_lista():
    precio=float(input('Cual es el precio con decimales:'))
    print('El valor es de:', int(precio), 'Euros', 'con' ,float(precio-int(precio)),'decimales')

precio_lista()
# Ejercicio 8

"""
    Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
    Mes Ventas Gastos
    Enero 30500 22000
    Febrero 35600 23400
    Marzo 28300 18100
    Abril 33900 20700
"""

import pandas as pd
Mes=['Enero','Febrero','Marzo','Abril']
Ventas=[30500, 35600,28300, 33900]
Gastos=[22000,23400,18100,20700]

df1=pd.DataFrame({"Mes": Mes,"Ventas": Ventas,"Gastos": Gastos})
df1

# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""

# Ejercicio 10

"""
    Escribir un programa que almacene las asignaturas de un curso
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    pregunte al usuario la nota que ha sacado en cada asignatura,
    y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
"""