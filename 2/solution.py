data = []
with open('input.txt', 'r', encoding='utf-8') as file1:
    for line in file1:
        data.append(line[:-1]) if line[0] == 'a' or line[0] == 'A' else data
with open('output.txt', 'w', encoding='utf-8') as file2:
    for el in data:
        file2.write(el)
        file2.write('\n')