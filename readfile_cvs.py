import csv
#Leer un archivo
"""with open('monthly_sales.csv', mode='r') as file:
    csv_reader= csv.DictReader(file)
    for row in csv_reader:
        print(row)"""

#Mostrar la informacion por columnas

with open('monthly_sales.csv', mode='r') as file:
    csv_reader= csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['month']}, Precio: {row ['sales']}")
        #en este ejemplo debes porner entre comillas el nombre de la columna que deseas imprimir
