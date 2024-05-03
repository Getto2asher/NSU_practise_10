with open('input.txt', 'r', encoding='utf-8') as file1:
    data = list(map(str.strip, file1.readlines()))
with open('output.txt', 'a+') as file2:
    try:
        if len(data) - 1 == int(data[0]):
            file2.write('YES')
        else:
            file2.write('NO')
    except ValueError:
        file2.write('ERROR')