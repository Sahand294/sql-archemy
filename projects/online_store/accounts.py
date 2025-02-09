from book_product import  BookProduct
from electronics import ElectronicProduct
from products import  Product
from passwords import  Passwords
from adding_account import  Adding_Account
Adding_Accounts = Adding_Account()
import csv
passwords = Passwords()
class Account:
    def __init__(self,customerid:int,password):
        self.cart = {}
        self.customer = customerid
        Adding_Accounts.adding(customerid,password)
        print('your account has succesfully been made')
    def change_password(self,old_password,new_password):
        if passwords.check_password(old_password,self.customer):
            passwords.change_password(self.customer,new_password)
        else:

            print(passwords.check_password(old_password,self.customer))
            raise ValueError('wrong password')
        print('you have succesfully changed your password')
    def add_product_to_cart(self,product,amount,password):
        if passwords.check_password(password,self.customer):
            pass
        else:
            raise ValueError('wrong password')
        if  isinstance(product,Product) or  isinstance(product,BookProduct) or  isinstance(product,ElectronicProduct):
            pass
        else:
            raise ValueError("no such product!")
        if product.stock < amount:
            raise ValueError(f"sorry but we don't have that many of them! ")
        if product.stock == 0:
            raise ValueError(f'sorry but we have  ran out!')
        self.cart[product.name] =  {'name':product.name,'price':(product.price * amount),'amount':amount}
        product.stock -= amount
        with open('purchase history.txt', 'a') as text:
            text.write(f"\n{self.customer} has bought {amount} of {product.name} and paid:{(product.price * amount)}")
        print('you have succesfully add the item to your cart')

    def review(self):
        return self.cart
    def remove_product(self,product,password):
        if passwords.check_password(password,self.customer):
            pass
        else:
            raise ValueError('wrong password')
        if product.name not in self.cart:
            raise ValueError("no such product!")
        del self.cart[product.name]
        with open('purchase history.txt', 'a') as text:
            text.write(f"\n{self.customer} has returned {product.name}")
        print('you have succesfully removed the product from your cart')
    def CalculatePrice(self):
        price = 0.0
        for i in self.cart:
            price += self.cart[i]['price']
        self.cart['final price'] = price