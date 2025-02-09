import sqlite3
connection = sqlite3.connect("mydatabase.db")
curser = connection.cursor()
curser.execute("update users set name = 'radin' where id = 1")
connection.commit()
connection.close()