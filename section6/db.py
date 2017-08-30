import pymysql.cursors
import pymysql
import os

class DB_Handler:
    DB_TYPE="mysql"
    DB_USERNAME = 'deepanshululla'
    DB_PASSWORD = '' #not required for c9
    DATABASE_NAME = 'flask_rest_db'
    DB_HOST = os.getenv('IP', '0.0.0.0')
    # DB_NAME='data.db'
    def __init__(self):
        self.connection = pymysql.connect(host= self.DB_HOST,    # your host, usually localhost
                     user=self.DB_USERNAME,         # your username
                     passwd=self.DB_PASSWORD,  # your password
                     db=self.DATABASE_NAME)        # name of the data base
        self.cursor = self.connection.cursor()
    
    def execute_query(self, query, query_tuple=None):
        if query:
            if query_tuple:
                self.cursor.execute(query,query_tuple)
                result=self.cursor.fetchall()
            else:
                self.cursor.execute(query)
                result=self.cursor.fetchall()
            return result
            
    def execute_query_fetch_one(self, query, query_tuple=None):
        if query:
            if query_tuple:
                self.cursor.execute(query,query_tuple)
                result=self.cursor.fetchone()
            else:
                self.cursor.execute(query)
                result=self.cursor.fetchone()
            return result
        
    def __del__(self):
        self.connection.commit()
        self.connection.close()
