number = int(input())
if number == 0:
    print(1)
    exit()
for i in range(1, number):
    number *= i
print(number)


