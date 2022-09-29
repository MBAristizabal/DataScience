

 #*1)** Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

#precio=int(input("Ingrese el valor del producto: "))
#descuento= int(input("Ingrese el descuento otorgado: "))
#porcentajeiva=int(input("indique el porcentaje a aplicar:"))
def descuento():
    pf= precio-(precio* (descuento/100))
    return pf
#print(descuento())

def iva():
    pb=precio*porcentajeiva
    return pb
#print(iva)

#2)** Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.

def func_lista(funcion, lista):
    lista_new=[]
    for i in lista:
        lista_new.append(funcion(i))
    return lista_new


def sumar(x):
    z=x+20
    return z

#print(func_lista(sumar,[2,3,6,1]))


#3)** Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

frase=input("Ingrese una frase : ")


def frase():
    
    keys=frase.split
    values=frase
    dicci={keys,values}
    
    for k ,v in dicci.items():
        return dicci
#print(frase())


#4)** Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
#    Escribir una función reciba una lista de notas y
 #   devuelva la lista de calificaciones correspondientes a esas notas.
  #  Suspenso < 5
   # Aprobado = 5
    #Suficiente entre 5 - 7
    #Notable 7-9
    #Sobresaliente > 9

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'
def apply_grade(scores):
    '''
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return list(map(grade, scores))

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))
# Descomentar para ejecutar:
# print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))


#**5)** Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    #Escribir una función que reciba un diccionario con las asignaturas y
    #las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas
    #y las calificaciones correspondientes a las notas.


#**6)** Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

    #Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
    #pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
    #por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

def password():
    key = "contraseña"
    password = input("Introduce la contraseña: ")
    if key == password.lower():
        print("La contaseña coincide")
    else:
        print("La contraseña no coincide")
        return "La contaseña coincide"
    return "La contraseña no coincide"

password()
# Descomentar para ejecutar:
#print(password())