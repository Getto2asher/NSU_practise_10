with open('input.txt', 'a+') as file:
    data = list(map(str.strip, file.readlines()))
    for el in data:
        file.write(el)
        file.write('\n')