ticket_storage = {'train':{'stock':16,
                                        'location':'st.johns',
                                        'date':'11/15/2024',
                                        'price':12,
                                        'sold':0},


                  'flight': { 'stock': 120,
                              'location': 'St. John\'s International Airport',
                              'date': '11/25/2024',
                              'price': 300,
                              'sold': 0 },



                  'taxi': { 'stock': 25,
                            'location': 'George Street',
                            'date': '11/19/2024',
                            'price': 10, 'sold': 0 },


                  'motorcycle rental': { 'stock': 15,
                                         'location': 'Water Street',
                                         'date': '11/20/2024', 'price': 50,
                                         'sold': 2 },


                  'scooter rental': { 'stock': 40,
                                      'location': 'Signal Hill',
                                      'date': '11/21/2024',
                                      'price': 7,
                                      'sold': 5 },



                  'helicopter tour': { 'stock': 8,
                                      'location': 'Quidi Vidi Lake',
                                       'date': '11/22/2024',
                                       'price': 500,
                                       'sold': 3 },



                  'boat tour': { 'stock': 30,
                                 'location': 'Harbourfront',
                                 'date': '11/23/2024',
                                 'price': 25, 'sold': 10 },



                  'horse carriage': { 'stock': 5,
                                      'location': 'Bannerman Park',
                                      'date': '11/24/2024',
                                      'price': 30, 'sold': 1 }}
moreinfo = []
class Info:
    def __init__(self,stock,location,date,price,soldcategoryname):
        self.stock = stock
        self.location = location
        self.date = date
        self.price = price
        self.sold = soldcategoryname
class RemainingCalcul:
    def __init__(self,stock,the_amount_sold,name,libarary,the_name_for_the_sold_category):
        if libarary[name][stock] == 0:
            print('non left!')
        else:
            libarary[name][stock] -= the_amount_sold
            libarary[name][the_name_for_the_sold_category] += the_amount_sold
class GettingTheInpuForBuying:
    def __init__(self,libarery):
        self.ticketname = input('what ticket do you want to buy:')
        self.amount = int(input('how many:'))
        self.name = self.ticketname
        self.stockname = 'stock'
        self.soldname = 'sold'
        RemainingCalcul(self.stockname,self.amount,self.name,libarery,self.soldname)


class Showing:
    def __init__(self,thename,library):
        print(library[thename])
class Choosing:
    def __init__(self,liberary):
        global truing
        choice = input('do you want to view or buy tickets. say a for view and b for buying:')
        if choice == 'b':
            GettingTheInpuForBuying(liberary)
        elif choice == 'a':
            view = input('which one:')
            Showing(view,liberary)
        elif choice == 'exit':
            truing = False
truing = True
while truing:
    Choosing(ticket_storage)


