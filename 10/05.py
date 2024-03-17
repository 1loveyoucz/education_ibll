n = int(input('Сколько солдат: '))
soldier_l = []
for i in range(n):
    soldier_l += [input()]
k = int(input('Номер кто будет получать наряд: '))
m = int(input('Сколько будет повторений: '))
for j in soldier_l:
    del soldier_l[k-1::3]
    print(*soldier_l, sep='\n')
    print(f'Каждому по {m} наряда вне очереди')
    break
