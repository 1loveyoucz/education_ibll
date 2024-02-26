n = int(input('Сколько чисел? - '))
answ = 0
plus_minus = 1
for i in range(n):
    n_1 = int(input(f'Число {i + 1}: '))
    answ += plus_minus * n_1
    plus_minus *= -1
print(f'Ответ: {answ}')