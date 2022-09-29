#Ejercicio 1

import pandas as pd

import matplotlib.pyplot as plt

#Dada estos valores: 15 16 17 16 21 22 15 16 15 17 16 22 14 13 14 14 15 15 14 15 16 10 19 15 15 22 24 25 15 16

df = pd.DataFrame({"Datos": [15, 16, 17, 16, 21, 22, 15, 16, 15,
 17, 16, 22, 14, 13, 14, 14, 15, 15,
 14, 15, 16, 10, 19, 15, 15, 22, 24,
 25, 15, 16,]})

df.head()

#1) histograma
def histograma(df, bin):
    plt.hist(df, bins=bin, color="green",
             histtype="bar", rwidth=0.25)
    plt.grid(True)
    plt.xlabel("Datos")
    plt.ylabel("Frecuencia")
    plt.title("Histograma con barra 2")

    plt.show()

histograma(df, 2)
#2) ¿Cuál es el número que más se repite?
#El 14 es el valor que más se repite

#3) ¿Qué pasa si cambiamos a tamaño de barra 5?
plt.hist(df.Datos,bins=5,
color="blue",
histtype="bar",
rwidth=0.25
)
plt.grid(True)
plt.xlabel("Datos")
# frequency label
plt.ylabel('Frecuencia')
# plot title
plt.title('histograma')
#plt.show()

#4) ¿Qué pasa si cambiamos a tamaño de barra 20?
plt.hist(df.Datos,bins=20,
color="blue",
histtype="bar",
rwidth=0.25
)
plt.grid(True)
plt.xlabel("Datos")
# frequency label
plt.ylabel('Frecuencia')
# plot title
plt.title('histograma')
#plt.show()
#print(df.Datos.value_counts())

# Si sacamos la frecuencia con value_counts vemos que obtenemos los datos que se representan en la distribución
#5) ¿Qué parece indicar el sesgo en la distribución?

#Que es sesgo positivo, tenemos valores atípicos hacia la derecha
