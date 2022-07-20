"""
1)- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una
función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""
def maximo(x,y):
    if x > y :
        return x
        print(f'el valor {y} es el valor maximo')
    else:
        return y 
        print(f'el valor {y} es el valor maximo')
    
maximo (2, 5)
maximo (10, 8)

