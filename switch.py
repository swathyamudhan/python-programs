def week(i):
    switcher = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    fun = switcher.get(i, "Invalid day of week")
    print(fun)


value = int(input())
week(value)

def add_customer_record():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        if conn.is_connected():
            cursor = conn.cursor()
            data_1 = input("Enter the sl no:")
            data_2 = input("Enter the first name :")
            data_3 = input("Enter the last name :")
            data_4 = input("Enter the tenure :")
            data_5 = input("Enter the date :")
            data_6 = input("Enter the loan_id(1-Home loan,2-Personal loan,3-Auto loan:")
            stmt = "insert into customer(id,first_name,last_name,tenure,loan_date,loan_id)values(%s,%s,%s,%s,%s,%s)"
            cursor.execute(stmt, (data_1, data_2,data_3,data_4,data_5,data_6))
            conn.commit()
            print("Updated the record!!!")
            cursor.execute("select * from customer")
            rows = cursor.fetchall()
            print("Total rows", cursor.rowcount)
            for row in rows:
                print(row)
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
