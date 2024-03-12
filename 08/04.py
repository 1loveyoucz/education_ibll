size = int(input("Размер доски (<=9) "))
for i in range(size, 0, -1):
    for j in range(size):
        print(f'{chr(65 + j)}{i}',end=' ')
    print()




