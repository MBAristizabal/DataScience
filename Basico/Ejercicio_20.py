# Ejercicios
#
# *1)** Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
entero=int(input('ingrese un numero : '))
caracter=input('ingrese un caracter: ')
def generar_caracteres(entero,caracter):
    
    resultado=entero * caracter
    return resultado

print(generar_caracteres(entero, caracter))



#**2)** Definir un diagrama procedimiento() que tome una lista de números enteros e imprima un diagrama en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

"****"

"*********"

"*******"

def procedimiento(lista):
    for i in lista:
        print(i * "x")

procedimiento([4, 9, 7])
# Descomentar para ejecutar:
# procedimiento([4, 9, 7])
#**3)** Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
def mas_larga(lista):
    mas_larga = ""
    for i in lista:
        if len(i) > len(mas_larga):
            mas_larga = i
    return mas_larga

#print(mas_larga(["coche", "tortuga", "bici"]))
# Descomentar para ejecutar:
# print(mas_larga(["coche", "tortuga", "bici"])
#**4)** Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
def filtrar_palabras(lista, n):
    listado = []
    for i in lista:
        if len(i) > n:
            print(i)
            listado.append(i)
    return listado

filtrar_palabras(["coche", "tortuga", "bici"], 4)
# Descomentar para ejecutar:
# print(filtrar_palabras(["coche", "tortuga", "bici"], 4))

#**5)** Escribir un programa que ingrese una cadenade texto. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
def c_mayusculas(cadena):
    cont = 0
    for i in cadena:
        if i != i.lower(): #Recordar que lower() convierte una cadena en minúsculas
            cont += 1
    print("La cadena tiene", cont, "mayuscula/s")
    return "La cadena tiene", cont, "mayuscula/s"

c_mayusculas("Mas que Coches")
# Descomentar para ejecutar:
# print(c_mayusculas("Mas que Coches"))

#**6)** Definir una tupla con 10 edades de personas.
#* Imprimir la cantidad de personas con edades superiores a 20.


#**7)** Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
#También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
def main():
    x = int(input("Cuantos nombres quieres ingresar?: "))
    lista = []
    for i in range(x):
        a = input("Ingresa el nombre: ")
        lista.append(a)   
        lista.append(a)
    print("\n")
    

    comienzo = input("Con que letra empieza el nombre?: ")
    cont = 0
    for i in lista:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper() :
            cont += 1
    return cont

main()
# Descomentar para ejecutar:
# print(main())


#**8)** Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
#Se puede hacer que el usuario sea quien elija la palabra.

def contar_vocales(palabra):
    palabra=input('ingrese palabra')
    palabra=palabra.lower()
    vocales='aeiou'
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador+=1    
    return contador

print(contar_vocales('palabra'))

