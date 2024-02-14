answer_1 = input('Вам нравится мультфильм "Пингвины из Мадагаскара"?: ')
answer_2 = input('Вам нравится персонаж Шрек?: ')
if answer_1.lower() == 'да' and answer_2.lower() == 'нет':
    print('У вас разносторонние интересы')
elif answer_1.lower() == 'нет' and answer_2.lower() == 'да':
    print('Вы целеустремленный')
elif answer_1.lower() == 'нет' and answer_2.lower() == 'нет':
    print('Вы откровенный')
elif answer_1.lower() == 'да' and answer_2.lower() == 'да':
    print('У вас отличный вкус')
else:
    print('Ошибка! Неверный ответ')

