import sqlite3
conection=sqlite3.connect("it.sl3", 5)
cur=conection.cursor()
#cur.execute("CREATE TABLE first_table (name Text);")
cur.execute("INSERT INTO first_table (name) VALUES('Andrey');")
conection.commit()
conection.close()