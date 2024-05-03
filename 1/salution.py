with open('input.txt') as file1:
    string = file1.read()

with open('output.txt', 'a+') as file2:
    string = str(string.upper())
    file2.write(string)
