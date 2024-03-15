n = int(input('Кол-во данных: '))
text_l = []
print('Поиск:')
for i in range(n):
    text = input()
    text_l += [text]
n_word = int(input('Кол-во поисковых строк: '))
word_l = []
for j in range(n_word):
    word = input('Поисковая строка: ')
    word_l +=[word]
for t in text_l:
    yes_no = True
    for word in word_l:
        if word not in t:
            yes_no = False
            break
    if yes_no:
        print(t)

