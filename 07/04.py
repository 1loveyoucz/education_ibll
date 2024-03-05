speak_1 = str(input('1 называет: '))
speak_2 = str(input('2 называет: '))
if speak_1[-1] == speak_2[0]:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')