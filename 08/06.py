long = int(input('Длина заголовка: '))
n = int(input('Кол-во заголовков: '))
text_l = ''
c = '...'
for i in range(n):
    text = input()
    if len(text) >= long:
        text_l += text[:long-3] + c + '\n'
    else:
        text_l += text + '\n'
print(text_l)
