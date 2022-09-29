import pandas as pd
import matplotlib.pyplot as plt

# EJERCICIO 1

# 1) Lee con pandas el archivo train.csv correspondiente al titanic dataset

df = pd.read_csv("C:/Users/Flia Defelippe/Documents/DataScience/Basico/src/train.csv")

# Descomentar para ejecutar:
#print(df)


"""
    2) Hacer un bucle for para automatizar las gráficas de pd.crosstab
    Se pide relacionar la columna Survived con Pclass, Sex y Embarked
    Nota:
    Se pide que dentro del bucle for se encuentre la gráfica requerida.
    Entonces, en una sola celda, tenemos 3 gráficas mostradas y todo automatizado.
"""


#print(pd.crosstab(df.Sex, df.Survived))
#figure = pd.crosstab(df.Sex, df.Survived).plot(kind="bar")
#plt.show()
features = ["Pclass", "Sex", "Embarked"]

def mostrar(features):
    for feature in features:
        figure = pd.crosstab(df[feature], df.Survived).plot(kind="bar")
        #plt.show()
#Descomentar para ejecutar:
 
#print(mostrar(features))

   # 3) Hacer una función para automatizar las gráficas de pd.crosstab
    #Se pide relacionar la columna Survived con Pclass, Sex y Embarked
    #NOTA:
    #Se pide definir una función (1 vez por ello)
    #y hacer llamadas a la función (3 en este caso, para: Pclass, Sex, Embarked)

def fun_crosstab(feature):
    pd.crosstab(df[feature], df['Survived']).plot(kind='Bar')
    #plt.show

#print(fun_crosstab('Pclass'))
#print(fun_crosstab('Sex'))
#print(fun_crosstab('Embarked'))


# EJERCICIO 2

# Ejercicio de obtener los valores que muestra el pd.crosstab de Sex y Pclass sin usar el propio pd.crosstab

# 1) Imprime nuevamente los primeros 5 valores

#print(df.head())


# 2) Usando value_counts() observa cuantos hombres y mujeres hay

    # (No hace falta plotear, simplemente mostrar los números de cada)

#print(df.Sex.value_counts())

# 3) Sin usar value_counts() observa cuantos hombres y mujeres hay (con un algoritmo)
contador_female=0
contador_male=0


for data in df.Sex:
        if data == "female":
            contador_female +=1
        else:
            data == "male"
            contador_male+=1
        
#print('Hay', contador_female, "mujeres", 'y', contador_male, "hombres")

 # 4) Ahora haz lo mismo de otra forma
#En esta ocasión se pide que:
#crees un dataframe con el formato del original,bajo la permisa que sea un dataframe con todo hombres (primeramente)
#y con todo mujeres (a continuación)
#(2 DataFrames por tanto)
#Y observes si el número de filas de ambos nuevos DataFrames coincide con los valores anteriores


df_hombres=df[df["Sex"]=="male"]
#print(df_hombres)
#print(df.loc[df["Sex"]=="male"])

df_mujeres=df[df["Sex"]=="female"]
#print(df_mujeres)

#print(df.loc[df["Sex"]=="female"])