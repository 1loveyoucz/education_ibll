n = int(input('Кол-во советов: '))
text_l = ''
print('Советы:')
for i in range(n):
    text = input()
    if 'не' in text[0:3].lower():
        text_l += text[3:] + '\n'
    else:
        text_l += text + '\n'
print(text_l)
