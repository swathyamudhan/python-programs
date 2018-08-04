def addition():
    print('The addition of two numbers')
    while True:
        try:
            value1 = float(input('Enter the first value '))
        except ValueError:
            print('Invalid number,enter again')
            continue
        while True:
            try:
                value2 = float(input('Enter the second value '))
            except ValueError:
                print('Invalid number,enter again')
                continue
            else:
                result = float(value1) + float(value2)
                print('sum of two numbers', result)
                break
        break


def subtraction():
    print('The Subtraction of two numbers')
    while True:
        try:
            value1 = float(input('Enter the first value '))
        except ValueError:
            print('Invalid number,enter again')
            continue
        while True:
            try:
                value2 = float(input('Enter the second value '))
            except ValueError:
                print('Invalid number,enter again')
                continue
            else:
                result = float(value1) - float(value2)
                print('subtraction of two numbers', result)
                break
        break


def calc(i):
    switcher = {
        "1": addition,

        "2": subtraction,

        "3": exit
    }
    return switcher.get(i,'Invalid option')


print('welcome to Calculator')
while True:
    try:
        print('Please select your option')
        option = input('1.Addition 2.Subtraction 3.Exit')
        calc_function = calc(option)
        calc_function()

    except TypeError:
        print("Invalid option")




