n = int(input('Кол-во строк: '))
for i in range(n):
    text = input()
    yes_no = False
    for j in range(len(text) - 2):
        if text[j:j + 3] == 'кот':
            print(f'{i + 1} {j + 1}')
            yes_no = True
            break
