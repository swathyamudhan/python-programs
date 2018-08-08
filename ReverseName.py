def reverse(name):
    # split word of the string by using space
    split_name = name.split(" ")
    length = len(split_name)
    first_part = split_name[length-1] + ','
    index = 0
    while index <= length-2:
        first_part = first_part + ' ' + split_name[index]
        index = index + 1
    return first_part


data = input('Enter the data to reverse the string')
output = reverse(data)
print(output)
