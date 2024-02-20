temperature = float(input('Введите температуру: '))
while temperature < 15.5:
    print('ХОЛОДНО')
    temperature = float(input('Введите температуру: '))
    while temperature > 28:
        print('ЖАРКО')
        temperature = float(input('Введите температуру: '))
        while 15.5 < temperature <28:
            print('НОРМАЛЬНО')
            break

