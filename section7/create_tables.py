import MySQLdb
import os
from db import DB_Handler


dbh= DB_Handler()
DATABASE_NAME = 'flask_rest_db'

# create_database="CREATE DATABASE IF NOT EXISTS {db_name}".format(db_name=DATABASE_NAME)
# dbh.execute_query(create_database)

create_table = "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(80) UNIQUE, password VARCHAR(100))"
dbh.execute_query(create_table)

# user = (1, 'bob', '123')
# insert_query= "INSERT INTO users VALUES (?,?)"
# cursor.execute(insert_query, user)

create_table = "CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(150) UNIQUE, price float)"
dbh.execute_query(create_table)

# dbh.execute_query("INSERT INTO items VALUES (?,?)",('laptop','700'))



