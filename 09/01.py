n = int(input('Сколько продуктов? '))
products_l = []
print('Продукты:')
for i in range(n):
    products = input()
    products_l += [products]
for product in products_l:
    print(product)