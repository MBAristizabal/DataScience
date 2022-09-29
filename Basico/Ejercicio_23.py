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

#class Alumno:

    #def __init__(self, nombre, edad, asignatura, nota):
       # self.nombre = nombre
        #self.edad = edad
        #self.asignatura = asignatura
        #self.nota = nota
#alumno1 = Alumno( "Juan", 17, "matematica", 7)
#alumno2 = Alumno( "Jose", 17, "biologia", 6)
#alumno3 = Alumno( "Lucas", 16, "quimica", 8)

#print(alumno3.edad)
#print(alumno3.nota)
#print(alumno2.edad)
#print(alumno2.nota)

# Ejercicio 2

"""
    Escribir un programa que pregunte al usuario su edad
    y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

def edad():
    age = int(input("¿Cuántos años tienes? "))
    for i in range(age):
        print("Has cumplido " + str(i+1) + " años")

#print(edad())


# Ejercicio 3

"""
    Escribir un programa que pida al usuario una palabra y
    luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
"""
#palabra=input("Ingrese una palabra: ")
#for i in range(len(palabra)-1,-1,-1):
    #print(palabra[i])
 
# Ejercicio 4

   # Escribir un programa que pregunte el nombre completo del usuario en la consola y
    #después muestre por pantalla el nombre completo del usuario tres veces,
    #una con todas las letras minúsculas,
    #otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
    #El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.


def nombre_completo():
    name = input("¿Cómo te llamas? ")
    print(name.lower())
    print(name.upper())
    print(name.title())

#print(nombre_completo())
# Ejercicio 5

"""
    Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
    y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato
    y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
def opcion1():
    tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
    print('El número de teléfono es ', tel[4:-3])
    return f'El número de teléfono es {tel[4:-3]}'

def opcion2():
    tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
    print('El número de teléfono es ', tel.split("-")[1])
    return f'El número de teléfono es {tel.split("-")[1]}'

#opcion1()
#opcion2()
# Descomentar para ejecutar:
# print(opcion1())
# print(opcion2())


# Ejercicio 6

"""
    Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
    y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
#frase=input('Ingrese  una frase: ')
#vocal=input('Ingrese vocal: ')

#if vocal in frase:
    #print(vocal.upper())
    #print(frase.replace(vocal,vocal.upper()))



# Ejercicio 7

#"""
    #Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
    #y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
#"""

#def precio_lista():
    #precio=float(input('Cual es el precio con decimales:'))
    #print('El valor es de:', int(precio), 'Euros', 'con' ,float(precio-int(precio)),'decimales')

#precio_lista()
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
def data():
    datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'],
            'Ventas':[30500, 35600, 28300, 33900],
            'Gastos':[22000, 23400, 18100, 20700]}
    contabilidad = pd.DataFrame(datos)
    print(contabilidad)
    # print(contabilidad)
    return contabilidad

contabilidad = data()
contabilidad1 = data()
# Ejercicio 9

"""
    Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
    una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.

"""
def balance(contabilidad, meses):
    contabilidad['Balance'] = contabilidad.Ventas - contabilidad.Gastos
    return contabilidad[contabilidad.Mes.isin(meses)].Balance.sum()

print(balance(contabilidad, ['Enero','Marzo']))
# Descomentar para ejecutar:
# print(balance(contabilidad, ['Enero','Marzo']))



# Ejercicio 10

   # Escribir un programa que almacene las asignaturas de un curso
    #(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
    #pregunte al usuario la nota que ha sacado en cada asignatura,
    #y después las muestre por pantalla con el mensaje "Has sacado ASIGNATURA la nota de NOTA"
    #donde es cada una de las asignaturas de la lista y cada una de las correspondientes notas introducidas por el usuario.
def subjects():
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    scores = []
    for subject in subjects:
        score = input("¿Qué nota has sacado en " + subject + "?")
        scores.append(score)
    for i in range(len(subjects)):
        print("En " + subjects[i] + " has sacado " + scores[i])

subjects()
# Descomentar para ejecutar:
# subjects()