from csv_handeling import CsvHandeling
class Product:
    def __init__(self,name,price,quantity,key):
        self.name = name
        self.price = price
        self.quantity = quantity
        CsvHandeling.adding(name,price,quantity,key)