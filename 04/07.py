number = int(input())
check = 0
for i in range(1,number+1):
    if number % i == 0:
        print(i, end=' ')
        check +=1
if check > 2:
    print('\nНЕТ')
else:
    print('\nПРОСТОЕ')




