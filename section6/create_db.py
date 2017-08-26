import MySQLdb
import os
from db import DB_Handler


dbh= DB_Handler()

create_table = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(80) UNIQUE, password VARCHAR(100))"
# INTEGER makes it automatically incrementing


dbh.execute_query(create_table)

# user = (1, 'bob', '123')
# insert_query= "INSERT INTO users VALUES (?,?)"
# cursor.execute(insert_query, user)

create_table = "CREATE TABLE IF NOT EXISTS items (name VARCHAR(150) UNIQUE PRIMARY KEY, price float)"
# real is floating number
dbh.execute_query(create_table)

# dbh.execute_query("INSERT INTO items VALUES (?,?)",('laptop','700'))



