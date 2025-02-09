import sqlite3
connection = sqlite3.connect("mydatabase.db")
curser = connection.cursor()
curser.execute("CREATE TABLE users('id' INTEGER PRIMARY KEY AUTOINCREMENT,'name' VARCHAR(999))")
connection.commit()
connection.close()