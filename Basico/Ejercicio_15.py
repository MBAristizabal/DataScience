import pandas as pd

# EJERCICIO 1


# 1) Crea una lista de nombre "Concursante" que contenga los siguientes valores:
    # "Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"
concursante=["Juan", "Pedro", "Andrea", "Luis", "Ana", "Lara", "Jose", "Estefania"]
#print(concursante)
# 2) Crea una lista de nombre "Resultados" que contenga los siguientes valores:
    # 20, 30, 50, 20, 10, 5, 60, 40
resultados=[20, 30, 50, 20, 10, 5, 60, 40]
#print(resultados)
# 3) Crea un diccionario con los concursantes y los resultados.
diccionario=(dict(zip(concursante, resultados)))
#print(diccionario)
# 4) Crea un dataframe vacio y apendiza los concursantes y los resultados mediante el empleo de un bucle for
listado_keys=[]
for key in diccionario.keys():
    listado_keys.append(key)
#print(listado_keys)

listado_values=[]
for value in diccionario.values():
    listado_values.append(value)
#print(listado_values)

df_diccionario=pd.DataFrame(listado_keys,columns=['concursante'])
#print(df_diccionario)
df_diccionario['resultados']= listado_values
#print(df_diccionario)

# 5) Con ayuda de loc filtra los resultados obtenidos desde Pedro hasta Lara.
#print(df_diccionario.loc[1:5, :])


# 6) Con ayuda de loc filtra los resultados obtenidos mayores o iguales a 40
#print(df_diccionario.loc[df_diccionario["resultados"]>40])


# 7) Muestra el concursante con la mayor puntuación
def maximo(df_diccionario):
    return"resultados".max()
#print(df_diccionario)

# 8) Muestra el concursante con la menor puntuación
#print(df_diccionario["resultados"].min())
#print(df_diccionario)
# 9) Modifica con la ayuda de loc los valores 20 por 0
df_diccionario.loc[df_diccionario["resultados"]==20, "resultados"]=0
#print(df_diccionario)
# 10) Modifica Concursante "Juan" su puntuación por "None" con ayuda de .loc
df_diccionario.loc[df_diccionario["concursante"]=="Juan", "resultados"]=None
#print(df_diccionario)


# EJERCICIO 2 (3)

"""
    Escribe un programa que pida dos palabras y diga si riman o no.
    Si coinciden las tres últimas letras tiene que decir que riman.
    Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
"""
#palabra1=input("ingrese una palabra:  ")
#palabra2=input("ingrese una palabra:  ")
def riman(palabra1, palabra2):
    

    for letra in palabra1:
        if palabra1[-3:]== palabra2[-3:]:
            print("las palabras riman")
        elif palabra1[-2:]== palabra2[-2:]:
            print("las palabras riman poco")
        else:
            print("las palabras no riman")
        return riman

#print(riman(palabra1,palabra2))
