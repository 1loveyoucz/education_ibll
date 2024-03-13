text_1 = str(input('строка №1 - '))
text_2 = str(input('строка №2 - '))
bull = 0
cow = 0
for i in range(len(text_1)):
    if text_1[i] == text_2[i]:
        bull +=1
    elif text_1[i] in text_2:
        cow +=1
print(f'БЫКС - {bull} КОРОВ - {cow}')

