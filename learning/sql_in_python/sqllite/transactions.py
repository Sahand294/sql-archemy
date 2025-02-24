import sqlite3
connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()
try:
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO user_temth(name,email) VALUES('you','hey')")
    cursor.execute("INSERT INTO user_temth(name,email) VALUES('you','hey')")
    connection.commit()
except sqlite3.IntegrityError as E:
    print(E)
   # connection.rollback()
finally:
    connection.close()