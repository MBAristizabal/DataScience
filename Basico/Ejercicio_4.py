# EJERCICIO 1

"""
    Crear un pequeño programa que calcule la multiplicación de 2 números (x, y)
    x = 3, y = 5
    x = 7, y = 3
"""
# a) Con una función (por ejemplo funcion_multiplicar)
def multiplicar(x,y):
    return (x*y)
    
#print(multiplicar(3,5))
#print(multiplicar(7,3))

# b) Con la función lambda (Tal vez puedes ir a repasarlo)
multiplica =lambda x,y : x*y
z =multiplica(3,5)
#print(z)

# c) Realizarlo con entrada de teclado (input)

#= int(input("Ingrese valor a multiplicar:  "))   

#print(multiplicar(x,y))



# EJERCICIO 2

"""
    -A-
        Dado un string:
        "Level"
        ¿Es un palíndromo?
"""
A ='Level'
def palindromo(A):
    A1 = []
    i = -1
    while len(A1) < len(A):
        A1.append(A[i])
        i -= 1
    return A1

#print(palindromo(A))

#comparamos las dos listas: usamos un contador(diferente) para comprobar caracter a caracter

def comparar(A,A1):
    diferente = 0
    for i in range(len(A)):
        if A[i]!= A1[i]:
            diferente += 1
    return diferente
numero_diferente = comparar(A,palindromo(A))
# analisis final:
def conclusion(numero_diferente):
    if numero_diferente == 0:
        print("Es palindromo")
    else:
        print("No es palindromo")
        print("Hay",numero_diferente, "elementos diferentes")

#print(conclusion(numero_diferente))


"""
    -B-
        ¿Y este string?
        "level"
        Nota: "Es un palíndromo si se invierte el orden del string, el resultado es exactamente el mismo"
"""
B ='level'

#print(palindromo(B))

numero_diferente = comparar(B, palindromo(B))
    
#print(conclusion(numero_diferente))


# EJERCICIO 3

"""
    Dado 2 strings:
    S1 = "Hi!"
    S2 = "Hello!"
    Imprimir las letras que son comunes
"""

s1 = "Hi!"
s2 = "Hello!"
#print(s1,s2)


def comunes(S1,s2):
    lista_comunes=[]
    comun= 0
    for i in s1:
        for j in s2:
            if i==j:
                lista_comunes.append(i)
                comun+=1
    print(comun)
    
    return lista_comunes
    
print(comunes(s1,s2))


