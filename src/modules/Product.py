class Product:
    def __init__ (self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
