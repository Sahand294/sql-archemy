from csv_handeling import CsvHandeling
from  sqllite import TrackingOrders
class Orders:
    def __init__(self,product_key,quantity):
        product = CsvHandeling.reading_products(product_key)
        t_price = Orders.total_price(float(product['price']),quantity)
        CsvHandeling.changing_quantity(product_key,quantity)
        TrackingOrders(product['key'],quantity,t_price)
    @staticmethod
    def total_price(price,quantity):
        u = float(price)*float(quantity)
        return u