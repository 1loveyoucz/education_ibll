n = 0
cat_found = False

while True:
    s = input("Введите строку или 'СТОП' для завершения: ")
    if s.lower() == 'стоп':
        break
    n += 1
    if 'кот' in s.lower():
        cat_found = True
        break

if cat_found:
    print(f"Кот был упомянут в строке номер {n}.")
else:
    print(-1)
