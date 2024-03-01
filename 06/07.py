n_list = int(input('Кол-во листов? '))
n_last_name = int(input('Кол-во фамилий? '))
all_last_name_s = set()
print('Фамилии')
for i in range(n_list):
    last_name_s = set()
    print(f'{i+1} лист')
    for j in range(n_last_name):
        student = input()
        last_name_s.add(student)
    if i == 0:
        all_last_name_s = last_name_s
    else:
        all_last_name_s &= last_name_s

if all_last_name_s:
    for c in all_last_name_s:
        print(c)
