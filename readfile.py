
#leer un archivo linea por linea
"""with open('texto.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#leer todas las lineas en una lista
"""with open('texto.txt', 'r') as file:
    lines = file.readlines()
    print (lines)"""
#to add info to a file
"""with open('texto.txt', 'a') as file:
    file.write ("\n\nBy: Ana")"""

#Sobreescribir el texto
"""with open('texto.txt', 'w') as file:
    file.write("\n\nBy: Ana")"""
