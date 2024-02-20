password = str(input('Придумайте пароль: '))
password_2 = str(input('Придумайте пароль: '))
if len(password) < 8:
    print('Короткий!')
    exit()
elif password_2 != password:
    print('Различаются')
else:
    print('OK')