n = int(input('Число названных города: '))
city_s = set()
print('Города: ')
yes_no = True
for i in range(n):
    city = str(input())
    if city in city_s:
        yes_no = False
        break
    city_s.add(city)
if yes_no:
    print('OK')
else:
    print('TRY ANOTHER')
