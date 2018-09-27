import mysql.connector
from mysql.connector import Error


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', database='example', user='root', password='root')
        print("We got the connection")
        if conn.is_connected():
            print("Success!!!Connected to the database")
    except Error as e:
        print("Error has occurred!!!!")
        print(e)
    # finally block always runs
    finally:
        conn.close()


connect()
