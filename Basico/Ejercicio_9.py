 #EJERCICIO 1

"""
    Dado este listado de números:
    -3, 150, 0, 499, 500, 1200, -350, 0, 750, 25
    Haz un pequeño algoritmo que haga lo siguiente:
    Si el número es negativo debe imprimir lo siguiente el valor es negativo
    Si es 0 debe imprimir un mensaje que indique: 0
    Si se encuentra entre 0 (no incluido) y 200 (si incluido), imprime 0,200
    Si se encuentra entre 200 (no incluido) y 500 (no incluido), debe imprimir (200, 500)
    Si es 500 debe continuar sin hacer nada
    Si se encuentra entre 500 (no incluido) y 1000 (no incluido) debe saltar automaticamente y dejar de testear (parar)
    Para el resto de números, debe decir: valor demasiado grande, desde 1000, en adelante
"""
listado=[-3, 150, 0, 499, 500, 1200, -350, 0, 750, 25]
# 1) Escribir en formato lista

#print(listado)

# 2) Haz el propio ejercicio de programación planteado

def test(listado):
    for i in range(len(listado)):
        if listado[i]<0:
            print("el valor ingresado es negativo")
        elif listado[i]==0:
            print("el valor es cero")
        elif listado[i]>0 and listado[i]<= 200:
            print("el valor ingresado se encuentra entre 0 y 200")
        elif listado[i]> 200 and listado[i]< 500:
            print("el valor ingresado se encuentra entre 200 y 500")
        elif listado[i]>500 and listado[i]<1000:
            break
        else:
            print("el numero es demasiado grande")
    return listado

#print(test(listado))

# EJERCICIO 2

# Dada la lista de nombre "listado" y de valores: 10, 20, 20, 30, 40, 40, 40

# 1) Crea la lista e imprimela
listado=[10, 20, 20, 30, 40, 40, 40]
#print(listado)
# 2) Haz un set de esa lista

#set(listado)
#print(set(listado))
# 3) Trata de buscar los números NO REPETIDOS de esa lista (sin usar set)

def no_repetidos(listado):
    norepetidos=[]
    for numero in listado:
        if numero not in norepetidos :
            norepetidos.append(numero)
    return norepetidos
#print(no_repetidos(listado))

# Pista: Puedes almacenar todo en una nueva lista



# EJERCICIO 3

# Dados estos clientes:

# Usando el continue/break

# Trata de averiguar si un cliente concreto se encuentra en la BBDD (Base de Datos)

# "Ana Pérez", "Juan García", "Andres Álvarez", "Luis Ramos", "Pedro Cadenas", "Estefanía Miguélez", "Alberto Delgado", "Susana Castro", "Luis González"

clientes=["Ana Perez", "Juan Garcia", "Andres Alvarez", "Luis Ramos", "Pedro Cadenas", "Estefania Miguelez", "Alberto Delgado", "Susana Castro", "Luis Gonzalez"]

def consulta(clientes):
    
    buscado=input("ingrese cliente a buscar :")
    for cliente in clientes:
        if buscado in clientes:
            return"cliente encontrado"     
            continue        
        else:      
            return"cliente no encontrado"
            break
            
#print(consulta(clientes))     


