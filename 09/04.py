n = int(input('Кол-во строк: '))
text_l = []
for i in range(n):
    text = str(input())
    text_l += [text]
n_parts = int(input('Сколько частей? '))
parts_l = []
for j in range(n_parts):
    part = int(input('Часть: '))
    parts_l +=[part]
for part in parts_l:
    print(text_l[part - 1])
