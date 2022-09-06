#EJERCICIO 1

"""
Dada una lista de nombre "listado" y con valores: 10,20,30,40,50
"""
# 1) Crea un pequeño programa capaz de conseguir el orden inverso de los números de "listado"

L=[10,20,30,40,50]

lista_inversa=[]

def inverso(lista_inversa):
    while len(L)>0:
        lista_inversa.append(L[-1])
        del L[-1]
        print(L, lista_inversa)

#inverso(lista_inversa)


# imprime nuevamente el listado para tenerlo "a mano"
# 10-20-30-40-50 (tengo)
# 50-40-30-20-10 (lo que busco)

# EJERCICIO 2

"""
    Programa que coge por teclado 5 números y los almacena en una lista
    Nota:
    debería estar en la misma celda
    Hazlo como puedas, discurre cómo sería..
"""

numeros=int(input("ingrese los numeros elegidos"))
lista=[]
def numlista(numeros):
    lista.append(numeros)
    print(lista)



numlista(numeros)


# EJERCICIO 3

"""
    Programa que coge por teclado una frase y es capaz de decir cuántas vocales hay
    Nota: asume que son letras minúsculas sin tildes.
"""

frase= input("Ingrese una frase")


# 1) Entrada de texto por teclado
# 2) Hazlo si puedes de varias formas
    # forma 1: contar vocales en palabra/frase
# 3) Hazlo de otra forma si se te ocurre..
    # forma 2

# EJERCICIO 4

"""
    Tablas de multiplicar:
    Haz algo tal que:
"""

# 1) Pregunta al usuario que tabla quiere multiplicar: <1 al 10>

# 2) Muestra los resultados de esta forma:

"""
        2 x 1 = 2
        2 x 2 = 4
        ...
        2 x 10 = 20
"""