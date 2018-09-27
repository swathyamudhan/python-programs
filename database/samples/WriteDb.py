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
            stmt = "update hello set id = %s where name = %s"
            cursor.execute(stmt, (103, 'Sun'))
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
