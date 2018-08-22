import datetime

#The strptime() takes such a string and parses it. Finally, it returns a time tuple. It takes two arguments

def obtain_date():
    valid = False
    while not valid:
        date1 = input("Enter the  date 1 in  dd/mm/yyyy: ")
        date2 = input("Enter the  date 2 in  dd/mm/yyyy: ")
        try:
            d1 = datetime.datetime.strptime(date1,"%d/%m/%Y")
            d2 = datetime.datetime.strptime(date2,"%d/%m/%Y")
            valid = True
        except ValueError:
            print("Invalid,pls  try again")
    diff_days = abs((d1-d2).days)
    if diff_days == 1:
        print(diff_days, " day")
    else:
        print(diff_days, " days")


obtain_date()




