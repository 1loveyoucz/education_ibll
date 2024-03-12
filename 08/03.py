user_name = input('Никнейм: ')
for i in user_name[:]:
    if not (i.isalnum() or i == '_'):
        print(f'Неверный символ {i}')
        break
else:
    print('OK')

