print('Загадайте число от 1 до 1000')
minn = 1
maxx = 1000
attempts = 0
while minn <= maxx and attempts < 10:
    hidden_number = (minn + maxx) // 2
    print(hidden_number)
    answer = input('Введите символ:\n<\n>\n=\n')
    if answer == '<':
        maxx = hidden_number - 1
    elif answer == '>':
        minn = hidden_number + 1
    elif answer == '=':
        print(f'Ваше число: {hidden_number}')
        break
    attempts += 1
else:
    print('Закончились попытки')
