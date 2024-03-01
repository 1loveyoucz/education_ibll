en = int(input('Англ: '))
gr = int(input('Нем: '))
last_name_en = set()
last_name_gr = set()
print('Фамилии учеников, изущающих англ: ')
for i in range(en):
    eng = input()
    last_name_en.add(eng)
print('Фамилии учеников, изущающих нем: ')
for j in range(gr):
    grm = input()
    last_name_gr.add(grm)
last_name_double = last_name_en & last_name_gr
if not last_name_double:
    print('NO')
else:
    print(f'Сколько учеников изучают несколько языков? - {len(last_name_double)}')