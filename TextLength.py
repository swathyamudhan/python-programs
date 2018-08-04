def text():
    char = 0
    word = 1
    for c in string:
        char = char+1
        if c == ' ':
            word = word+1
    print('Number of words in the string:')
    print(word)
    print('The length of the text character is :')
    print(char)


string = input('Enter a text :')
text()

while True:
    data = input('Do you want to continue, (Y/N) ?')
    if data == 'y' or data == 'Y':
        string = input('Enter a text :')
        text()
    else:
        break
