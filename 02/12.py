import math
messange = str(input('Введите сообщение: '))
kop = 40*len(messange)
balance = kop%100
if len(messange) >= 3:
    rybles = math.floor(kop / 100)
    if balance ==0:
        print(f'Стоимость вашего сообщение составило: {rybles} руб.')
    else:
        print(f'Стоимость вашего сообщение составило: {rybles} руб. {balance} коп.')
else:
    print(f'Стоимость вашего сообщение составило: {balance} коп.')


