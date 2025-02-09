class InvetoryCreator:
    def __init__(self):
        self.inventory = {}

    def addproduct(self, product_name, price, quantity, category):
        self.name = product_name
        self.price = price
        self.quantity = quantity
        self.inventory[product_name] = {'name': product_name, 'price': price, 'quantity': quantity,
                                        'category': category}

    def restock(self, product_name, amount_to_be_added):
        self.inventory[product_name]['quantity'] += amount_to_be_added

    def selling(self, product_name, amount_to_be_sold):
        if self.inventory[product_name]['quantity'] == 0 or self.inventory[product_name][
            'quantity'] < amount_to_be_sold:
            print('non left!')
        else:
            self.inventory[product_name]['quantity'] -= amount_to_be_sold

    def ubdateing_price(self, product_name, new_price):

        self.inventory[product_name]['price'] = new_price


class Search:
    def name(self, dictionary, productame):
        print(dictionary[productame])

    def price(self, dictionary, price):
        for i in dictionary:
            if dictionary[i]['price'] == price:
                print(dictionary[i])

    def review(self, dictionary):
        for i in dictionary:
            print(dictionary[i], 'price to buy them all:', (dictionary[i]['price'] * dictionary[i]['quantity']))


class addremove:
    def add(self, dictionary, product_name, quantity, price, category):
        dictionary[product_name] = {'name': product_name, 'price': price, 'quantity': quantity, 'category': category}

    def remove(self, dictionary, product_name):
        del dictionary[product_name]



inven = InvetoryCreator()
product1 = inven.addproduct('Laptop', 1200, 10, 'tech')
product2 = inven.addproduct('Monitor', 300, 15, 'tech')
product3 = inven.addproduct('Keyboard', 50, 50, 'tech')
product4 = inven.addproduct('Mouse', 25, 75, 'tech')
product5 = inven.addproduct('Printer', 150, 20, 'tech')
search = Search()
search.price(inven.inventory, 50)

