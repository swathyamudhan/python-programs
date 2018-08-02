import os
from os import path
# Get name
# Name should have minimum of 2 characters and maximum of 256 characters
print('Please,Enter your name')
name = input()
nLen = len(name)
while nLen < 2 or nLen > 256 or name.isnumeric():
    print('Invalid name,pls enter again')
    name = input()
    nLen = len(name)


# Get age
# Age should be minimum of 1 and maximum of 150
print('Enter your age')
while True:
    try:
        age = int(input())
    except ValueError:
        print('Invalid age,please try again')
        continue
    else:
        if age < 1 or age > 150:
            print('Invalid age,please try again')
            continue
        break


# Get mobile number
print('Enter your mobile no.')
mNumber = input()
mLen = len(mNumber)
# Mobile number must be 10 characters and must be numeric
# If the mobile no. should be 10 digits and only numeric values otherwise user again type the correct values
while mLen != 10 or not mNumber.isnumeric():
    print('Please enter a valid mobile number')
    mNumber = input()
    mLen = len(mNumber)
    if mLen < 10:
        print('Your number is too short,enter again')
    elif mLen > 10:
        print('Your number is too high ,enter again')

# Get email id
print('Enter your Email id')
email = input()

# Display them all
print('**** Preview your information ****')
print(' Your name is :', name)
print(' Your age is :',age)
print(' Your Mobile number is :', mNumber)
print(' Your Email id is :', email)


basepath = path.dirname(path.abspath(__file__))
dataPath = path.join(basepath,'data')
#print(datapath)
if not path.exists(dataPath):
    os.makedirs(dataPath)
filepath = path.join(dataPath,'registration.txt')
helloFile = open(filepath,'a')
helloFile.write(str(name) + ' ' + str(age) + ' ' + str(mNumber) + ' ' + str(email) + ' ' +'\n')
helloFile.close()