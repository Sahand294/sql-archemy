import sqlite3
connection = sqlite3.connect("mydatabase.db")
curser = connection.cursor()
curser.execute("DROP TABLE users")

connection.commit()
connection.close()