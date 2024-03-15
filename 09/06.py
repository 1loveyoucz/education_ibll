n = int(input('Сколько вводится чисел? '))
n_l = []
for i in range(n):
    nnn = int(input('Число: '))
    n_l += [nnn]
for j in range(len(n_l) - 1):
    print(int(n_l[j]) + int(n_l[j+1]))