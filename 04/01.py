temperature = []
temperature_1 = float(input())
while temperature_1 < 22.0:
    temperature += [temperature_1]
    temperature_1 = float(input())
d = 0
for d in len(temperature):
    d += 1
    print(float(d))
