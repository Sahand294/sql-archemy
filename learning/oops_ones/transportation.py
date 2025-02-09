class Info:
    def __init__(self,type,name,capacity,price,miles):
        self.type = type
        self.name = name
        self.capacity = capacity
        self.price = price
        self.miles = miles

class CalculatorOfDecission:
    def milesperhour(self,miles,pricepermile,name):
        self.finalprice = miles * pricepermile
        CalculatorOfDecission.final(name,name,self.finalprice)
    def final(self,name,price):
        print(f'with a {name} it will cost you ${price} to get to your destination')
class FiguringOut:
    def __init__(self,type,name,miles,price):
        self.name = name
        self.miles = miles
        if type == 'matters':
            FiguringOut.milesperhour(self,price)
        else:
            FiguringOut.doesntmatter(self,price)
    def milesperhour(self,price):
        self.price = price
        CalculatorOfDecission.milesperhour(self, self.miles, self.price, self.name)
    def doesntmatter(self,price):
        self.prices = price
        CalculatorOfDecission.final(1,self.name,self.prices)
taxi = Info("doesn't matter",'bus',3,3,16)
FiguringOut(taxi.type,taxi.name,taxi.miles, taxi.price)

