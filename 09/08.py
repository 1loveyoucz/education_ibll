n = int(input('Количество дней: '))
syp = ['щи', 'борщ', 'щавелевый суп', 'суп овсяный', 'суп по-чабански']
c = []
for i in range(n):
    print(syp[i % len(syp)], end='\n')
