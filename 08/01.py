maxx = ''
minn = ''
while True:
    text = input()
    if not maxx or len(text) > len(maxx):
        maxx = text
    if not minn or len(text) < len(minn):
        minn = text
    if 'стоп' == text.lower():
        break
if set(minn) <= set(maxx):
    print('Да')
else:
    print('Нет')

