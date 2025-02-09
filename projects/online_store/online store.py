from book_product import  BookProduct
from electronics import ElectronicProduct
from products import  Product
from occasions import occasions
from discount import Discounts
from accounts import Account




book = BookProduct(100.0,'books','book',10)
phone = ElectronicProduct(500.0,'phones','apple',90)
christmas = occasions('christmas',50)
account1 = Account(19,'hi')
account1.add_product_to_cart(book,2,'hello')
Discounts(account1,christmas)
print(account1.review())
