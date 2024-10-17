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