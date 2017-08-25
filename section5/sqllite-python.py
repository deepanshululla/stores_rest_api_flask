import sqlite3
import os

try:
    os.remove("data.db")
    print("File removed")
except:
    print("Starting fresh..")

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table_query = "CREATE TABLE users (id int, username text, password test)"

cursor.execute(create_table_query)

user = (1, 'bob', '123')

insert_query= "INSERT INTO users VALUES (?,?,?)"

users = [
        (2,"relf","asdf"),
        (3, "anne", "xyz")
    ]


cursor.execute(insert_query, user)
cursor.executemany(insert_query, users)
connection.commit()

select_query = "SELECT * from users"
for row in cursor.execute(select_query):
    print(row)


# pushes data to db
connection.close()
# closes connection
