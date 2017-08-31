import pymysql.cursors
import pymysql
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DB_Handler:
    def __init__(self):
        self.DB_TYPE="mysql"
        self.DB_USERNAME = 'deepanshululla'
        self.DB_PASSWORD = '' #not required for c9
        self.DATABASE_NAME = 'flask_rest_db'
        self.DB_HOST = os.getenv('IP', '0.0.0.0')
        self.connection = pymysql.connect(host= self.DB_HOST,    # your host, usually localhost
                    user=self.DB_USERNAME,         # your username
                    passwd=self.DB_PASSWORD,  # your password
                    db=self.DATABASE_NAME)        # name of the data base
        self.cursor = self.connection.cursor()
        
        
    def execute_query(self, query, query_tuple=None):
        try:
            if query:
                if query_tuple:
                    self.cursor.execute(query,query_tuple)
                    result=self.cursor.fetchall()
                else:
                    self.cursor.execute(query)
                    result=self.cursor.fetchall()
                return result
        except Exception as e:
            print("Error:"+e)
            print("Query:"+query)
                
    def execute_query_fetch_one(self, query, query_tuple=None):
        try:
            if query:
                if query_tuple:
                    self.cursor.execute(query,query_tuple)
                    result=self.cursor.fetchone()
                else:
                    self.cursor.execute(query)
                    result=self.cursor.fetchone()
                return result
        except Exception as e:
            print("Error:"+e)
            print("Query:"+query)    
        
    def __del__(self):
        self.connection.commit()
        self.connection.close()
