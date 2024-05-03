with open('input.txt', 'r', encoding='utf-8') as file1:
    data = list(map(str.strip, file1.readlines()))
with open('output.txt', 'a+') as file2:
    for el in data:
        if len(el) > 20:
            file2.write(el)
            file2.write('\n')