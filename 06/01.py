n_1_s = set()
n_2_s = set()
print('Первый лист: ')
while True:
    n = input()
    if n == "":
        break
    n_1_s.add(n)
input('Достаём 2 лист (нажмите enter)')
print('Второй лист:')
while True:
    n = input()
    if n == "":
        break
    n_2_s.add(n)
n_double = n_1_s & n_2_s
if not n_double:
    print('EMPTY')
else:
    for n in n_double:
        print(n)
