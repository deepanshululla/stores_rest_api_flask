import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# INTEGER makes it automatically incrementing

cursor.execute(create_table)

# user = (1, 'bob', '123')
# insert_query= "INSERT INTO users VALUES (?,?)"
# cursor.execute(insert_query, user)

create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
# real is floating number
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('laptop',700.99)")


connection.commit()
connection.close()