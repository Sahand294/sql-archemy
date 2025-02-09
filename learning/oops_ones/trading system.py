store = {}
bo = True


class Sell:
    def __init__(self, product, price, amount):
        store[product] = {'price': price, 'stock': amount}


class Buy:
    def __init__(self, product, amount):
        store[product]['stock'] -= amount


class Choice:
    def __init__(self):
        boo = True
        while boo:
            choice = input(
                'do you want to sell to the store or buy from the store or view the store or exit the store:')
            if choice == ('sell'):
                self.productname = input('put the product name:')
                self.productprice = int(input(f'put the {self.productname} price:'))
                self.productstock = int(input(f'put the {self.productname} amount:'))
                Sell(self.productname, self.productprice, self.productstock)
            elif choice == 'buy':
                self.productname = input('put the product name:')
                self.productstock = int(input('put the product amount you want to buy:'))
                Buy(self.productname, int(self.productstock))
            elif choice == 'view':
                print(store)
            elif choice == 'exit':
                boo = False
            else:
                pass


Choice()
