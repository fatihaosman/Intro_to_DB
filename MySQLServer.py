#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    #!Try to connect and run MySQL commands.If anything fails, jump to except.”
    #!This connects Python to the MySQL server, NOT a database
    try:  
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""
        )
        #!A cursor is like a pen:
        #!It sends SQL commands to MySQL
        #!It receives results (not used here)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    # except Error as e:
    #     print(f"Error connecting to MySQL: {e}")
    except mysql.connector.Error as e:
       print(f"Error connecting to MySQL: {e}")


    finally:
       if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
