import mysql.connector
from mysql.connector import Error


def connect():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(host='localhost', database='example', user='root', password='root')
        if conn.is_connected():
            print("Success!!!Connected to the database")
            cursor = conn.cursor()
            data_1 = input("Enter the name :")
            data_2 = input("Enter the value :")
            stmt = "insert into hello(name,id)values(%s,%s)"
            cursor.execute(stmt,(data_1,data_2))
            conn.commit()
            print("Updated the record!!!")
            cursor.execute("select * from hello")
            rows = cursor.fetchall()
            print("Total rows", cursor.rowcount)
            for row in rows:
                print(row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


connect()
