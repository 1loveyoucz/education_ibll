n_white = int(input('Пункты белого списка: '))
white_l = []
print('~БЕЛЫЙ СПИСОК~')
for i in range(n_white):
    white_z = input()
    white_l += [white_z]
print('~Чёрный список~')
n_black = int(input('Пункты чёрного списка: '))
black_l = []
for i in range(n_black):
    black_z = input()
    black_l += [black_z]
for w in white_l:
    for b in black_l:
        if b == w:
            print(w)