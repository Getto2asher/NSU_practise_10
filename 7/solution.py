with open('input.txt') as file:
    data = list(map(str.strip, file.readlines()))

with open('input.txt', 'w') as file1:
    for el in data:
        if el != '100':
            file1.write(el)
            file1.write('\n')