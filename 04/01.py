temperature_1 = float(input())
temperature = []
while temperature_1 < 22.0:
    temperature += [temperature_1]
    temperature_1 = float(input())

if len(temperature) >= 7:
    weeks = len(temperature) // 7
    print(f'Количество недель: {weeks}')
else:
    print(0)
