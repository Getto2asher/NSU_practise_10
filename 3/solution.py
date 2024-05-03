data = []
with open('input.txt', 'r', encoding='utf-8') as file1:
    data = file1.readlines()
with open('output.txt', 'a+', encoding='utf-8') as file2:
    for el in data:
        file2.write(el[0])
    