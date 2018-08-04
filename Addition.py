#Calculator

print('The addition of two numbers')
while True:
    try:
        value1 = int(input('Enter the first value '))
        value2 = int(input('Enter the second value '))
    except ValueError:
        print('Invalid number,enter again')
        continue
    else:
        addition = float(value1) + float(value2)
        print('sum of two numbers', addition)
    while True:
        option = input('Do you want to continue ? confirm Y or N')
        if option == 'Y'or option == 'y':
            proceed = True
            break
        elif option == 'N' or option == 'n':
            proceed = False
            break
            #exit(0)
        else:
            print('Invalid option')
    if proceed:
        continue
    else:
        break
