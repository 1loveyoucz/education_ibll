numbers = []
number = int(input())
while number > 0:
    numbers += [number]
    number = int(input())
for element in numbers:
    print(element)
