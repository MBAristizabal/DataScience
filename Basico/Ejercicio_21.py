# EJERCICIO 1

"""
    Escriba una función es_bisiesto() que determine si un año determinado es un año
    bisiesto. Un año bisiesto es divisible por 4, pero no por 100.
    También es divisible por 400.
"""
año=[]

def es_bisiesto():
    naconsultar=int(input('ingrese el año: '))
    if naconsultar %4==0:
         
        print(naconsultar, ': el año es bisiesto')
    else:
        print('el año no es bisiesto')

#print(es_bisiesto())





# EJERCICIO 2

"""
    Haz un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años.
    Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos
    esos años si cada año se aplica la tasa de interés introducida.
    Recordar que un capital C dolares a un interés del x por cien durante n años
    se convierte en C * (1 + x/100)elevado a n (años). Probar el programa
    sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
"""
def inversiones():
    C=int(input('ingrese la cantidad a invertir:  '))
    ti=float(input('ingrese tasa de interes: '))
    n=int(input('ingrese plazo en años: '))
    resultado= C * ((1 + ti/100)**n)
    return resultado

#print(inversiones())


# EJERCICIO 3

"""
    Este programa muestra primero el listado de categorías de películas
    y pide al usuario que introduzca el código de la categoría de la película
    y posterior a ello pide que el usuario introduzca el número de días de atraso,
    y así se muestra al final el total a pagar.
"""
#CATEGORIA       #PRECIO  CODIGO  RECARGO/DIA DE ATRASO
# FAVORITOS      2.50      1          0.50
# NUEVOS         3.00      2          0.75
# ESTRENOS       3.50      3          1.00
# SUPER ESTRENOS 4.00      4          1.50


while True:

    print("/n")
    print("**********MENU*************")
    print("*******1.Favoritos*********")
    print("*******2.Nuevos************")
    print("*******3.Estrenos**********")
    print("*******4.Super Estrenos****")
    print("******99.Salir del Menú****")
    print("***************************")
    print("/n")

    opcion=int(input("Inserte una opcion: "))
    if opcion ==1:
        diasatraso=int(input("Ingrese dias de retraso"))
        total=2.50+(0.50 * diasatraso)
        print("El monto a pagar es: ", total)
    elif opcion ==2:
        diasatraso=int(input("Ingrese dias de retraso"))
        total=3+(0.75*diasatraso)
        print("El monto a pagar es: ", total)
    elif opcion==3:
        diasatraso=int(input("Ingrese dias de retraso"))
        total=3.50+(1*diasatraso)
    print("El monto a pagar es: ", total)
    if opcion==4:
        diasatraso=int(input("Ingrese dias de retraso"))
        total=4+(1.50*diasatraso)
        print("El monto a pagar es: ", total)
    if opcion==99:
        break
    else:
        print("Por favor seleccione una opcion correcta")
        print("/")  

    



