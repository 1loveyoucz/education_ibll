step = int(input('Шаг: '))
code_1 = str(input('Послание: '))
for i in code_1:
    i = ord(i) + step
    print(chr(i),end='')