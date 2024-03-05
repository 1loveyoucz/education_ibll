speak_1 = str(input('Город - '))
while True:
    speak_2 = input('Город -  ')
    if speak_1[-1] == speak_2[0]:
        speak_1 = speak_2
    else:
        print(speak_2)
        break
