import sqlite3
connection = sqlite3.connect('prodb.db')
cursor = connection.cursor()
#cursor.execute('CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY AUTOINCREMENT,customername TEXT,amount INTEGER)')
#cursor.executemany('INSERT INTO orders(customername,amount) VALUES(?,?)',[
 #   ('ali',11),
  #  ('sarah',99)
#])
customer = "'alice');DROP TABLE orders;--"
amount = 500
text = 'INSERT INTO ORDERS(customername) VALUES (' + customer + ')'

cursor.execute(text)
connection.commit()
connection.close()