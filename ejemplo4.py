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