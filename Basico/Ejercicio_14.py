import pandas as pd
# EJERCICIO 1
"""
    Cada número es la suma de los 2 anteriores:
    0-1-1-2-3-5-8-13-21-34...
    Se pide programar esa secuencia con Python.
    Nota:
    Apendiza elementos hasta tener 10 primeros resultados.
    (los 10 números indicados desde 0 hasta 34)
    Si sabes, hazlo de varias formas diferentes
"""

def fibonacci():
    L = [0, 1]
    while (len(L) < 10):
        L.append(L[-1] + L[-2])
    return L

# print(fibonacci())



# EJERCICIO 2

# Cada número es la suma de los 2 anteriores:
# 0-1-1-2-3-5-8-13-21-34...

#Se pide programar esa secuencia con Python.
    #Nota:
    #Apendiza elementos hasta tener 10 primeros resultados.
    #(los 10 números indicados desde 0 hasta 34)
    #Si sabes, hazlo de varias formas diferentes
# Se pide programar para los números de fibonacci mayores de 1000
# Primero muestra los valores de 0 hasta 1000000, crea una lista
# con ese listado crea una segunda lista con los mayores de 1000

listado_fibo=[]
p,q =0,1

listado_fibo.append(p)
listado_fibo.append(q)

while len(listado_fibo)<10:
    p= p+q
    listado_fibo.append(p)
    q=p+q
    listado_fibo.append(q)
#print(listado_fibo)

while len(listado_fibo)<30:
    p= p+q
    listado_fibo.append(p)
    q=p+q
    listado_fibo.append(q)
#print(listado_fibo)



listado1000=[]

for numero in listado_fibo:
    if numero >1000:
        listado1000.append(numero)

#print(listado1000)


# EJERCICIO 3
# Se pide crear un NUEVO dataframe para cada uno de los siguientes casos
# planteados y que están relacionados con el Titanic DataSet
# (antes debéis de cargar el archivo como df)
# 1) Leer el archivo train.csv del titanic dataset
df = pd.read_csv("C:/Users/Flia Defelippe/Documents/DataScience/Basico/src/train.csv")


# Descomentar para ejecutar:
print(df)
# 2) Crear un dataframe de nombre df_sobreviven refiriéndose a un dataframe en el que todos los pasajeros sobreviven
# NOTA: si al principio no estás seguro del resultado, puedes usar value_counts() para comprobar tu resultado

print(df.value_counts())

df_sobreviven=df.Survived.value_counts()
#
#print(len(df.Survived))


df_sobreviven = df[df["Survived"] == 1]
#print(df_sobreviven)


# 3) Crear un dataframe de nombre df__no_sobreviven refiriéndose a un dataframe en el que NINGUNO de los pasajeros sobrevive
df_nosobreviven = df[df["Survived"] == 0]
#print(df_nosobreviven)

# 4) DataFrame de hombres que no sobrevivieron en el titanic
df_hombres_nosobreviven=df[(df["Survived"]==0) & (df["Sex"]=="male")]
#print(df_hombres_nosobreviven.head())

# 5) DataFrame de hombres que si sobrevivieron en el titanic
df_hombres_sobreviven=df[(df["Survived"]==1) & (df["Sex"]=="male")]
#print(df_hombres_sobreviven.head())
# 6) DataFrame de mujeres que no sobrevivieron en el titanic
df_mujeres_nosobreviven=df[(df["Survived"]==0) & (df["Sex"]=="female")]
#print(df_mujeres_nosobreviven)


# 7) DataFrame de mujeres que si sobrevivieron en el titanic
df_mujeres_sobreviven=df[(df["Survived"]==1) & (df["Sex"]=="female")]
#print(df_mujeres_sobreviven)