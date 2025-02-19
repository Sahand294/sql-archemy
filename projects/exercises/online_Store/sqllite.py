import sqlite3
from datetime import datetime

class TrackingOrders:
    def __init__(self,product_key,quantity,total_price):
        now = datetime.now()
        connection = sqlite3.connect('orders.db')
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO orders(product_key,price, quantity, date) VALUES ('{product_key}',{total_price},{quantity}, '{now.strftime('%Y-%m-%d %H:%M:%S')}')")
        connection.commit()
        connection.close()