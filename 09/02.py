n = int(input('Кол-во данных: '))
text_l = []
print('Поиск:')
for i in range(n):
    text = input()
    text_l += [text]
word = input('Поисковая строка: ')
for t in text_l:
    if word in t:
        print(t)

