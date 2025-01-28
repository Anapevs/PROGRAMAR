import statistics

import csv

# leer los datos de ventas mensuales 
monthly_sales = {}

with open('monthly_sales.csv', mode = "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list (monthly_sales.values())

print("Ventas mensuales: ", sales)

#Hallar la media de las ventas

mean_sales = int(statistics.mean(sales))
print(f"Media de las ventas: {mean_sales}")

#Hallar la mediana de las ventas

median_sales = statistics.median(sales)
print(f"Media de las ventas: {median_sales}")

#Hallar la moda de las ventas

mode_sales = statistics.mode(sales)
print(f"Media de las ventas: {mode_sales}")

#Hallar la desviación estándar de las ventas
standard_deviation_sales = statistics.stdev(sales)
print(f"Desviación estándar de las ventas: {standard_deviation_sales}")

#Hallar la varianza de las ventas
variance_sales = statistics.variance(sales)
print (f"Varianza de las ventas: {variance_sales}")

#Maximo de ventas
max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales

'''Media: Promedio aritmético de un conjunto de datos. Se calcula sumando todos los valores y dividiendo por el número total de valores.

Mediana: Valor central de un conjunto de datos ordenado. Si el número de datos es impar, es el valor del medio; si es par, es el promedio de los dos valores centrales.

Moda: Valor que ocurre con mayor frecuencia en un conjunto de datos. Puede haber más de una moda (multimodal) o ninguna si todos los valores tienen la misma frecuencia.

Desviación estándar: Medida de la dispersión de un conjunto de datos respecto a la media. Es la raíz cuadrada de la varianza y proporciona una medida de cuánto se desvían los datos en promedio de la media.

Varianza: Promedio de las desviaciones al cuadrado de cada valor respecto a la media. Es una medida de la dispersión de los datos. También es el cuadrado de la desviación estándar.

Rango: Diferencia entre el valor máximo y el valor mínimo en un conjunto de datos. Mide la extensión total de los valores.'''

