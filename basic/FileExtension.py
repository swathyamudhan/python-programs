def extension(data):
    try:
        text, ext = data.split(".")
        return ext
    except ValueError:
        return 'Invalid data'


content = input('Enter the file name with Extension')
output = extension(content)
print(output)

