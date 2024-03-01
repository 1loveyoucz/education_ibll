n = int(input("Введите количество строк: "))
yes_no = False

for i in range(n):
    s = input("Введите строку: ")
    if 'кот' in s.lower():
        yes_no = True
if yes_no:
    print("МЯУ")
else:
    print("НЕТ")
