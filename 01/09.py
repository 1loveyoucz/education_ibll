login = input('Введите логин: ')
backup_email = input('Введите резервный адрес эл.почты: ')
if '@' not in login and '@' in backup_email:
    print('ОК')
elif '@' in login:
    print('Некорректный логин')
else:
    print('Некорректный эл.адрес')