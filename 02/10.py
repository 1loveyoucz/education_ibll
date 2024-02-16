number_1 = float(input('Введите число: '))
number_2 = float(input('Введите число: '))
symbols = str(input('Выберите арифмитическое действие:\n+\n-\n*\n/\n'))
if symbols == '+':
    print(f'Ответ: {number_1 + number_2}')
elif symbols == '-':
    print(f'Ответ: {number_1 - number_2}')
elif symbols == '*':
    print(f'Ответ: {number_1 * number_2}')
if symbols == '/':
    if number_2 != 0:
        print(f'Ответ: {number_1 / number_2}')
    else:
        print('Ответ: 888888')
else:
    print('Ответ: 888888')
