a = int(input())
b = int(input())
while a < b:
    for i in range(a, b+1):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0:
            print('Fizz')
        else:
            print(i)
    break

