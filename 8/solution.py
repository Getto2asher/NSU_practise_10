with open('input.txt', 'r', encoding='utf-8') as file:
    data = list(map(str.strip, file.readlines()))
# print(data)
with open('output.txt', 'a+') as file1:
    cnt = 0
    control = 0
    for m in range(12):
        if m % 2 == 0 and m != 2:
            for d in range(31):
                cnt += int(data[control])
                control += 1
            file1.write(str(cnt/31))
            file1.write('\n')
            cnt = 0
        else:
            for d in range(30):
                cnt += int(data[control])
                control += 1
            file1.write(str(cnt/30))
            file1.write('\n')
            cnt = 0
print(control)