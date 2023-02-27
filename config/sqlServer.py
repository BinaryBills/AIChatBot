#Author: BinaryBills
#Creation Date: January 8, 2022
#Date Modified: January 17, 2022
#Purpose: Functions used to open an active connection and send data to the Wamp server.

import mysql.connector
from mysql.connector import Error
from config import settings


def connectToServer(host_name, user_name, user_password):
    """
    Given a SQL server, it connects to it and accesses 
    its information. 
    Source: https://realpython.com/python-sql-libraries/#mysql_1
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        exit()
    return connection

def connectToDatabase(host_name, user_name, user_password, db_name):
    """
    Given a SQL server with a database specified by the user, 
    it connects to it and accesses its information. 
    Source: https://realpython.com/python-sql-libraries/#mysql_1
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database = db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
        exit()
    return connection

def mysqli_query(connection, query):
    """
    Given a SQL server and a SQL command, it sends a query to the server.
    This function is intended to handle the creation of new SQL tables.
    #Source: https://realpython.com/python-sql-libraries/#mysql_1
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Command '{}' processed successfully".format(query))
    except Error as e:
        print(f"The error '{e}' occurred")

async def mysqli_user_query(connection, query, params):
    """
    Given a SQL server and a SQL command, a query is sent to the server.
    This function is intended to handle user messages.
    #Source: https://realpython.com/python-sql-libraries/#mysql_1
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print(f"Command '{query}' processed successfully")
        return cursor.lastrowid
    except Exception as e:
        print(f"The error '{e}' occurred")



