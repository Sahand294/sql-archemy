from connection_curser import Cots
import psycopg2

c = Cots()
connection = c.connection
cursor = c.cursor
try:
    connection.autocommit = False
    cursor.execute("BEGIN TRANSACTION")
    cursor.execute("INSERT INTO user_table(name,email) VALUES('you','hey')")
    cursor.execute("INSERT INTO user_table(name,email) VALUES('you','hey')")
    connection.commit()
except psycopg2.Error as E:
    print(E)
    connection.rollback()
finally:
    connection.close()
    cursor.close()
