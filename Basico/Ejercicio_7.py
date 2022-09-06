# EJERCICIO 1

"""
    Dado: "np.arange(2,10)"
    sigue los siguientes pasos:
    1) Escribe esa instrucción y asígnaselo a la variable "a"
"""
import numpy as np

a=np.arange(2,10)
#print(a)

# 2) ¿Es equivalente a "np.arange(2,10,1)"?
b=np.arange(2,10,1)
#print(b)

# 3) Se pide quedarse con aquellos números menores de 5.

    # hazlo con numpy si puedes para la variable "a"

menor5=0

for numero in a :
    if numero<5:
        menor5 +=1
#print("los numeros menores a 5 son:", menor5)

# 4) Hazlo pasando esa información (de "a") a una lista

lista_menores=[]

for numero in a :
    if numero<5:
        lista_menores.append(numero)
#print(lista_menores)


# 5) En base a los resultados..

    # ¿Es posible recorrer 1 a 1 un array de numpy?

# 6) Haz el mismo proceso programando una sola línea (toma "a" como referencia)

# EJERCICIO 2

"""
    Para estos valores (v de valores por abreviar):
    v1 = 4
    v2 = 5
    v3 = 7
    v4 = 8
    El objetivo será calcular la media de estos valores
    Para ello sigue los siguientes pasos:
"""

# 1) Imprime los valores de esas variables v1,v2,v3,v4
v1 = 4
v2 = 5
v3 = 7
v4 = 8

#print(v1) 
#print(v2)
#print(v3) 
#print(v4)
    
# 2) Descomenta las 2 líneas siguientes para aprender..

    #que es posible asignar varios valores en la misma línea

    # Y la asignación de valores a variables se hace de forma consecutiva.

v1,v2,v3,v4 = 4, 5, 7, 8
#print(v1,v2,v3,v4)

#3) Descomenta la línea siguiente para aprender una posible forma de calcular la media.

    #  Usamos nuevamente numpy..

media_numpy = np.mean([v1,v2,v3,v4])
#print(media_numpy)


# 4) Calcula la media sin usar numpy

    # Si el resultado no sale bien, razona cómo debería hacerse..

media= (v1+v2+v3+v4)/4
#print(media)


# EJERCICIO 3

"""
    Factorial de un número
    Nota:
    El Factorial de 5, por ejemplo:
    5! = 5 * 4 * 3 * 2 * 1 = 120
    y el de 3:
    3! = 3 * 2 * 1 = 6
    y así para todos..
    PASOS A SEGUIR Y COSAS A TENER EN CUENTA
    Pide por teclado el número del cual quieres calcular el factorial.
    Para que no sea muy grande te recomendamos:
    3,4 o 5 (para hacer las pruebas)
    si ya no lo recuerdas o nunca lo viste, no te preocupes..
    3! es: 3 * 2 * 1 = 6
    4! es: 4 * 3 * 2 * 1 = 24
    5! es: 5 * 4 * 3 * 2 * 1 = 120
    (esto es lo que se pide, en esencia)
"""

f_a_calcular=int(input("elige el factorial a calcular:"))
x=np.arange(1,f_a_calcular+1)
print(x)
def factor(f_a_calcular):
    factorial1= 1
    
    return f_a_calcular * factorial1 * x

print(factor(f_a_calcular))

# EJERCICIO 4

"""
    Haz un cronómetro en Python:
    Obviamente:
    Horas - Minutos - Segundos
    Debes usar lo siguiente (from time import sleep)
    NOTA: Si quieres puedes usar sleep(0.000001)
    en vez de sleep(1) -> 1 segundo
    (para no esperar 1 segundo a ver los cambios)
    Para poder pararlo en poco tiempo,
    imprime mientras horas<2, cuando llegue a 2 debería parar la ejecución.
    Debería ejecutarse en unos 2 minutos aprox.
"""