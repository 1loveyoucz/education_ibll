n = int(input('Кол-во чисел: '))
n_l = []
for i in range(n):
    n_l.append(int(input('Число: ')))
nn = int(input('Результат: '))
yes_no = False
for i in range(n):
    for j in range(i+1, n):
        if n_l[i] * n_l[j] == nn:
            yes_no = True
if yes_no:
    print('ДА')
else:
    print('НЕТ')
