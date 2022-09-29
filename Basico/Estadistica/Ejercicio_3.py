 #EJERCICIO 1

"""
    En 2007-2008, la altura promedio de un jugador de baloncesto profesional fue de 2,00 metros con una desviación estándar de 0,02 metros. 
    Harrison Barnes es un jugador de baloncesto que mide 2,03 metros. ¿Qué porcentaje de jugadores son más altos que Barnes?
"""
µ = 2.00
x = 2.03
s = 0.02
def Zscore(µ,x,s):
    return round((x-µ)/s, 2)
#print(Zscore(2.00,2.03,0.02))
# El 93.32 son mas 
#Buscamos en la tabla de Z score: 1.5 y 0.0, nos da como resultado 0.9332, como nos pide cual es el
#porcentage de los mas altos sería:
def  mas_altos():
    mas_altos =1-0.9332
    return mas_altos*100

print(mas_altos())

#El 6.80% es mas alto

# EJERCICIO 2

# Chris Paul mide 1,83 metros. ¿Qué proporción de jugadores de baloncesto se encuentran entre las alturas de Paul y Barnes?


µ = 2.00
x = 1.83
s = 0.02

Zscore = round((x-µ)/s, 2)
#print(Zscore)
# El resultado es -8.4. Cuando el valor de z es de -4 tiende a cero

# EJERCICIO 3

"""
    El 92 % de los candidatos obtuvo una puntuación tan buena o peor que la de Steve.
    Si el puntuación promedio fue 55 con una desviación estándar de 6 puntos, ¿cuál fue el puntuación de Steve?
"""
µ = 55
s = 6
porcentage = 0.9200
Zscore= 1.41
#Buscamos en la tabla el valor de 0.9200 o próximo, vemos que es 1.41

x = (Zscore * s) + µ
#print(x)

#La puntuacion de Steve fue del 63.46%