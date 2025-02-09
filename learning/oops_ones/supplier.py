from datetime import datetime


class Suppliers:
    def __init__(self, product:str, supply_year:int, supply_month:int, supply_day:int, price:int, name:str, lists:list):
        self.procuct = product
        self.name = name
        self.date = datetime(supply_year, supply_month, supply_day).strftime("%Y-%m-%d")
        self.price = price
        lists.append({'supplier name': name, 'product': product, 'the price for the product': price, 'date': self.date,
                      'date1': datetime(supply_year, supply_month, supply_day)})


# .strftime("%y-%m-%d")
class Reviews:
    def __init__(self, lists):

        for i in lists:
            print(i)


class Search:
    def product(self, lists, product):
        for i in lists:
            if i['product'] == product:
                print(i)

    def name(self, lists, name):
        for i in lists:
            if i['supplier name'] == name:
                print(i)

    def price(self, lists, price):
        for i in lists:
            if i['the price for the product'] == price:
                print(i)

    def date(self, lists, whattype):
        if whattype == 'specific date':
            date = input('what date:')
            for x in lists:
                if x['date'] == date:
                    print(x)
        elif whattype == 'bettween':
            firstdate = datetime(int(input('start:what is the year for bettween:')),
                                 int(input('start:what is the month for bettween:')),
                                 int(input('start:what is the day for bettween:')))
            lastdate = datetime(int(input('end:what is the year for bettween:')),
                                int(input('end:what is the month for bettween:')),
                                int(input('end:what is the day for bettween:')))
            for i in lists:
                if i['date1'].year > firstdate.year:
                    if i['date1'].month > firstdate.month:
                        if i['date1'].day > firstdate.day:
                            if i['date1'].year < (lastdate.year + 1):
                                if i['date1'].month < (lastdate.month+1):
                                    if i['date1'].day < (lastdate.day+1):
                                        print(i)


# def everything(self,lists,product,name,price,whatttype):

suppliers = []
supplier1 = Suppliers('laptop', 2024, 11, 15, 500, 'supplier1', suppliers)
supplier2 = Suppliers('monitor', 2024, 12, 1, 200, 'supplier2', suppliers)
supplier3 = Suppliers('keyboard', 2025, 1, 10, 300, 'supplier3', suppliers)
supplier4 = Suppliers('mouse', 2025, 2, 14, 150, 'supplier4', suppliers)
supplier5 = Suppliers('printer', 2025, 3, 5, 400, 'supplier5', suppliers)
supplier6 = Suppliers('scanner', 2025, 4, 20, 250, 'supplier6', suppliers)
supplier7 = Suppliers('desk', 2025, 5, 25, 100, 'supplier7', suppliers)
supplier8 = Suppliers('chair', 2025, 6, 18, 180, 'supplier8', suppliers)
supplier9 = Suppliers('webcam', 2025, 7, 22, 120, 'supplier9', suppliers)
supplier10 = Suppliers('tablet', 2025, 8, 30, 350, 'supplier10', suppliers)
supplier11 = Suppliers('smartphone', 2025, 9, 13, 600, 'supplier11', suppliers)
supplier12 = Suppliers('headphones', 2025, 10, 5, 220, 'supplier12', suppliers)
supplier13 = Suppliers('microphone', 2025, 11, 7, 110, 'supplier13', suppliers)
supplier14 = Suppliers('projector', 2025, 12, 20, 700, 'supplier14', suppliers)
supplier15 = Suppliers('speaker', 2025, 1, 15, 260, 'supplier15', suppliers)
supplier16 = Suppliers('router', 2025, 2, 28, 80, 'supplier16', suppliers)
supplier17 = Suppliers('switch', 2025, 3, 21, 300, 'supplier17', suppliers)
supplier18 = Suppliers('server', 2025, 4, 10, 1200, 'supplier18', suppliers)
supplier19 = Suppliers('desktop', 2025, 5, 14, 900, 'supplier19', suppliers)
supplier20 = Suppliers('hard drive', 2025, 6, 30, 500, 'supplier20', suppliers)
supplier21 = Suppliers('memory card', 2025, 7, 23, 100, 'supplier21', suppliers)

searching = Search()
searching.date(suppliers,'bettween')
