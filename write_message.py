filename='programming.txt'
with open(filename) as file_object:
    contents=file_object.read()
    print(contents)