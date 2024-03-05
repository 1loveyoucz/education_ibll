ingr = int(input('Кол-во ингридиентов: '))
prod_s = set()
while True:
    for i in range(ingr):
        prod = input()
        prod_s.add(prod)
    print(ingr - 1)
    for j in range(ingr - 1):
        print('бутерброд')
        print(ingr)
    for elem in prod_s:
        print(elem)
