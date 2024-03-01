n = 0
yes_no = False
while True:
    s = input("Введите строку или 'СТОП' для завершения: ")
    if s.lower() == 'стоп':
        break
    n += 1
    if 'кот' in s.lower():
        yes_no = True
        break
if yes_no:
    print("МЯУ")
else:
    print("НЕТ")
