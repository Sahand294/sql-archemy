import sqlite3
connection = sqlite3.connect('mydatabase.db')
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
cursor.execute('SELECT * FROM users')
output = cursor.fetchall()
for i in output:
    print(dict(i))
connection.close()