import sqlite3
connection = sqlite3.connect("mydatabase.db")
curser = connection.cursor()
curser.execute("insert into users('name') values ('sahand'),('radman')")
connection.commit()
connection.close()
# ALTER TABLE CITY ALTER COLUMN ids  TYPE BIGINT USING ids::bigint;