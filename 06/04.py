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
symm_diff = last_name_en ^ last_name_gr
if not symm_diff:
    print('NO')
else:
    print(f'Сколько учеников изучают один язык? - {len(symm_diff)}')