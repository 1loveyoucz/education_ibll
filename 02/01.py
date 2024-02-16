city_1 = input('Введите 1 город: ')
city_2 = input('Введите 2 город: ')
if city_1 == 'Тула' and city_2 == 'Тула':
    print('НЕТ')
elif city_1 == 'Тула' and city_2 == 'Пенза':
    print('НЕТ')
elif city_1 == 'Пенза' and city_2 == 'Тула':
    print('НЕТ')
elif city_1 == 'Пенза' and city_2 == 'Пенза':
    print('НЕТ')
else:
    print('ДА')