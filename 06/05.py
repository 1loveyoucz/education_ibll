en = int(input('Англ: '))
gr = int(input('Нем: '))
fr = int(input('Франц: '))
last_name_en = set()
last_name_gr = set()
last_name_fr = set()
print('Фамилии учеников, изущающих англ: ')
for i in range(en):
    eng = input()
    last_name_en.add(eng)
print('Фамилии учеников, изущающих нем: ')
for j in range(gr):
    grm = input()
    last_name_gr.add(grm)
print('Фамилии учеников, изущающих франц: ')
for c in range(fr):
    frm = input()
    last_name_fr.add(frm)

last_name_with_two_lang = last_name_en & last_name_gr | last_name_en & last_name_fr | last_name_gr & last_name_fr
if not last_name_with_two_lang:
    print('NO')
else:
    print(f'Сколько учеников изучают 2 языка? - {len(last_name_with_two_lang)}')
