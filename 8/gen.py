import random
with open('input.txt', 'w') as file:
    for m in range(12):
        if m % 2 == 0 and m != 2:
            for d in range(31):
                file.write(str(random.randint(400, 13000)))
                file.write('\n')
        else:
            for d in range(30):
                file.write(str(random.randint(400, 13000)))
                file.write('\n')