message = str(input('Приём, приём я 2: '))
n = int(input('Какую букву будем вытаскивать? '))
if n > len(message):
    print('ОШИБКА')
else:
    for j in range(len(message)):
        i = j + 1
        print(str(message[n - i]))
        break
