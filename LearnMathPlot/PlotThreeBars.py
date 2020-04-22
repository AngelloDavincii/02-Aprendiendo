import numpy as np
from matplotlib import pyplot as plt

#ESTE COMANDO ME PERMITE VER LOS TIPOS DE GRAFICAS DISPONIBLES
#print(plt.style.available)
plt.style.use("fivethirtyeight")#USAMOS EL TIPO DE GRAFICA QUE NOS GUSTA


# Median salary by age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

#Le asigna un indice a cada coso que use ages_x
#Sirve para hacer 2 o 3 barras
x_indixes = np.arange(len(ages_x))
#Le pone un ancho a la barra
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indixes - width, dev_y , width = width,color = "#444444", linestyle = "--",label = "All devs")

# Median Python Developer Salaries by Age

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


plt.bar(x_indixes, py_dev_y, width = width,label = "python")#Se imprime otra linea en la misma grafica

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indixes+width, js_dev_y, width = width,label = "JavaScript")


plt.xlabel("Ages")#Le pone titulo al eje x
plt.ylabel("Median Salary")#titulo al eje y
plt.title("Median Salary (USD) by Age")#Titulo general

plt.legend()#Le pone nombre a cada linea

#ajusta bien el eje x con las barras
plt.xticks(ticks=x_indixes,labels = ages_x)

#Le agrega grid a grafica
#plt.grid(True)

plt.tight_layout()#No se que hace xD

#Guarda imagen en el directorio actual
plt.savefig("plot.png")

plt.show()


