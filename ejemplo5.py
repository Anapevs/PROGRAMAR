empleados = [
    {'nombre': 'Juan', 'edad': 35, 'sueldo': 35000},
    {'nombre': 'Ana', 'edad': 25, 'sueldo': 40000},
    {'nombre': 'Pedro', 'edad': 30, 'sueldo': 30000},
    {'nombre': 'María', 'edad': 40, 'sueldo': 45000},
    {'nombre': 'Luis', 'edad': 35, 'sueldo': 38000},
    {'nombre': 'Carmen', 'edad': 27, 'sueldo': 39000},
    {'nombre': 'Carlos', 'edad': 45, 'sueldo': 50000}
]

mayor_sueldo = []

def empleados_mayor_sueldo ():
    for empleado in empleados:
        if empleado['sueldo'] >= 40000:
            mayor_sueldo.append ((empleado['edad'], empleado['nombre'], empleado['sueldo']))

empleados_mayor_sueldo()


print(f"Empleados con sueldo mayor: ")
for edad, nombre, sueldo in mayor_sueldo:
    print(f"Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo}")


'''employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

def filter_salary():
    """
    Filtra a los empleados que ganan más de 4000 USD

    Sin parámetros

    Retorna:
    list: Una lista de empleados
    """
    return list(filter(lambda employe: employe['salary'] >= 4000, employees))

print(f'Esta es la lista de todos los empleados: {employees}')
print(f'Los empleados que ganan 4000 o más USD al mes son: {filter_salary()}')'''