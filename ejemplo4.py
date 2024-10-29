class Vehicle :
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.isAvailable = True
    def sell (self):
        if self.isAvailable :
            self.isAvailable = False
            print (f"El vehiculo {self.brand} ha sido vendido")
        else:
            print (f"El vehiculo {self.brand} no esta disponible")

    def check_available (self):
        return self.isAvailable
    
    def get_price (self):
        return self.price
    
    def start_engine (self):
        raise NotImplementedError ("Este metodo debe ser implementado por la subclase")
    
    def stop_engine (self):
        raise NotImplementedError ("Este metodo debe ser implementado por la subclase")

class Car (Vehicle): 
    def start_engine (self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
            
    def stop_engine (self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no esta disponible"
        
class Bike (Vehicle):
    def start_engine (self):
        if not self.is_available:
            return f"La bicicleta {self.brand} esta en marcha"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
            
    def stop_engine (self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no esta disponible"
        
class Truck (Vehicle):
    def start_engine (self):
        if not self.is_available:
            return f"El camión {self.brand} esta en marcha"
        else:
            return f"El camión {self.brand} no esta disponible"
            
    def stop_engine (self):
        if self.is_available:
            return f"El camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no esta disponible"
class Customer:
        def __init__(self, name):
            self.name = name
            self.pucharsed_vehicle = []
        def buy_vehicle(self, vehicle: Vehicle):
            if vehicle.check_available():
                vehicle.sell()
                self.pucharsed_vehicle.append(vehicle)
            else:
                print(f'Lo siento, {vehicle.brand} no esta disponible')
        
        def inquire_vehicle(self,vehicle: Vehicle):
            if vehicle.check_available():
                availability = "Disponible"
            else:
                availability = "No disponible"
            print (f"El {vehicle.brand} esta {availability} y cuesta {vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles (self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print (f"El {vehicle.brand} ha sido añadido al inventario")

    def registre_customers(self, customer: Customer):
        self.customers.append(Customer)
        print(f'El cliente {customer.name} ha sido añadido')

    def show_available_vehicle(self):
        print ("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available ():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")

car1 = Car ("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "FH", 800)
truck1= Truck ("Volvo", "MZ-U", 80000)

customer1 = Customer ("Frank Suarez")

dealer = Dealership ()
dealer.add_vehicles (car1)
dealer.add_vehicles (bike1)
dealer.add_vehicles (truck1)

dealer.show_available_vehicle()