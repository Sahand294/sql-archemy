class Customers:
    def __init__(self):
        self.database = {}
    def addingcustomers(self,customer_name,id,contact_number):
        self.points = 0
        self.dollars_spent = 0
        self.amount_of_purchases = 0
        self.database[customer_name] = {'name:':customer_name,'id:':id,'contact name:':contact_number,'amount of purchases':self.amount_of_purchases,'loyalty points':self.points}

    def adding_purchases(self,customer_name,purchase_data,amount_of_dollars_Spent):
        self.database[customer_name][f'purchase {self.amount_of_purchases+1}'] = f'{purchase_data}'
        dollars = amount_of_dollars_Spent
        for i in range(amount_of_dollars_Spent):
            if dollars >= 10:
                self.database[customer_name]['loyalty points'] += 1
                dollars -= 10
        self.database[customer_name]['amount of purchases'] += 1
        self.amount_of_purchases += 1
class Search:
    def name(self,database,name):
        for i in database:
            if i == name:
                print(database[i])
    def id(self,database,id):
        for i in database:
            if database[i]['id:'] == id:
                print(database[i])

customers = Customers()
customer1 = customers.addingcustomers('customer1',1335678,85837)
customers.adding_purchases('customer1','laptop for 800',800)
customers.adding_purchases('customer1','food for 100',100)
customer2 = customers.addingcustomers('customer2',5758279275,37464946)
customers.adding_purchases('customer2','mouse for 20',20)
search = Search()
search.id(customers.database,1335678)