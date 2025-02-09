class Product:
    def __init__(self, amount, price, name):
        self.names = name
        self.stock = amount
        self.price = price

    def setdiscount(self, discountpercantage):
        self.discount = Discount(discountpercantage)

    def finlnum(self):
        return self.discount.apply(self.price)


class Discount:
    def __init__(self, discountpercentag=10):
        self.percantage = discountpercentag

    def apply(self, price):
        return round(price * (1 - self.percantage), 2)


class Store:
    def __init__(self):
        self.products = []

    def add_products(self, product):
        self.products.append(product)

    def add_products_from_dict(self, productdata):
        for name, details in productdata.items():
            self.add_products(name)

    def remove_products(self, product):
        self.products.remove(product)

    def show_store(self):
        return self.products
p1 = Product(50,20,'mouse')
p2 = Product(30,15,'alive_golden_fish')
store = Store()
store.add_products(p1)
store.add_products(p2)
showing = store.show_store()
for i in showing:
    print(i.names,'\n',i.price,'\n',i.stock)
