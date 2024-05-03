with open('input.txt', 'r') as file1:
    data = list(map(str.strip, file1.readlines()))

with open('output.txt', 'a+') as file2:
    try:
        answer = int(data[0]) / int(data[1]) + int(data[2])
        file2.write(str(answer))
    except ZeroDivisionError:
        file2.write('Division by 0')
    except ValueError:
        file2.write('data error')