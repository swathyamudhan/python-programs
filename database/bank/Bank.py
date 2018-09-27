import mysql.connector
import datetime
from mysql.connector import Error


def get_connection():
    conn = mysql.connector.connect(host='localhost', database='Bank', user='root', password='root')
    return conn


def display_records_from_db(sql):
    cursor = None
    conn = None
    try:
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            print("Total rows", cursor.rowcount)
            for row in rows:
                print(row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def execute_sql(sql, data):
    cursor = None
    conn = None
    try:
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            print(cursor.rowcount,'Record updated successfully and id is ',cursor.lastrowid)
    except Error as e:
        print("Failed inserting record {}".format(e))
    finally:
        cursor.close()
        conn.close()


def validate(date_text, data):
    try:
        datetime.datetime.strptime(date_text,'%Y-%m-%d')
    except ValueError:
        raise ValueError("Exception raised. Incorrect date format, should be YYYY-MM-DD. User details"+ str(data))


def delete_record(sql, cust_id):
    cursor = None
    conn = None
    try:
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql, cust_id)
            conn.commit()
            print('Record deleted successfully')
    except Error as e:
        print("Failed deleting record {}".format(e))
    finally:
        cursor.close()
        conn.close()


def search_record(sql, criteria):
    cursor = None
    conn = None
    try:
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(sql, criteria)
            for rows in cursor.fetchall():
                print(rows)
            if cursor.rowcount == 0:
                print('no record found in database')
    except Error as e:
        print("Failed in searching record {}".format(e))
    finally:
        cursor.close()
        conn.close()


def view_customer_records():
    sql = 'select * from customer'
    display_records_from_db(sql)


def view_loan_records():
    sql = 'select * from loan'
    display_records_from_db(sql)


def add_customer_record():
    first_name = input("Enter the first name :")
    last_name = input("Enter the last name :")
    tenure = input("Enter the tenure :")
    loan_date = input("Enter the date in YYYY-DD-MM :")
    loan_type = input("Enter the loan_id(1-Home loan,2-Personal loan,3-Auto loan:")
    data = (first_name, last_name, tenure, loan_date, loan_type)
    sql = "insert into customer(first_name,last_name,tenure,loan_date,loan_id)values(%s,%s,%s,%s,%s)"
    execute_sql(sql, data)


def delete_customer_record():
    cust_id = int(input("Enter the id:"))
    sql = "delete from customer where id = %s"
    delete_record(sql, (cust_id,))


def search_customer_id():
    search_id = int(input("Enter the id:"))
    sql = "select * from customer where id=%s"
    search_record(sql, (search_id,))


def search_customer_first_name():
    search_fname = input("Enter the first name:")
    sql = "select * from customer where first_name=%s"
    search_record(sql, (search_fname,))


def search_customer_last_name():
    search_lname = input("Enter the last name:")
    sql = "select * from customer where last_name=%s"
    search_record(sql, (search_lname,))


def get_all_customer_by_loan_type():
    loan_type = input("Enter the loan type either 1(Home loan)/2(Personal loan)/3(Auto loan):")
    sql = "select * from customer where loan_id = %s"
    search_record(sql, (loan_type,))


def process_input(i):
    switcher = {
        1: view_loan_records,
        2: view_customer_records,
        3: add_customer_record,
        4: delete_customer_record,
        5: search_customer_id,
        6: search_customer_first_name,
        7: search_customer_last_name,
        8: get_all_customer_by_loan_type
    }
    return switcher.get(i, 'Invalid option')


print('Bank Records')
print('Select your option')
input_value = int(input('1.View Loan records\n2.View Customer records\n3.Add customer record\n4.Delete customer records\n'
                        '5.Search_customer by id\n6.Search customer by firstname\n7.Search customer lastname\n'
                        '8.Get all Customer based on loan type'))
bank_process = process_input(input_value)
if type(bank_process).__name__ == 'str':
    print(bank_process)
else:
    bank_process()






