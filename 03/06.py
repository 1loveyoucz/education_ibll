password = input('Придумайте пароль: ')
password_2 = input('Подтвердите пароль: ')
while '123' in password or len(password) < 8 or password_2 != password:
    if '123' in password:
        print('Простой!')
    if len(password) < 8:
        print('Короткий!')
    if password_2 != password:
        print('Различаются.')
    password = input('Придумайте пароль: ')
    password_2 = input('Подтвердите пароль: ')
print('OK')

