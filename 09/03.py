n = int(input('Кол-во строк: '))
text_l = []
for i in range(n):
    text = input()
    text_l += [text]
nb = int(input('Номер буквы: '))
for j in text_l:
    if len(j) >= nb:
        print(j[nb-1],end='')
    else:
        print()