height_b = float(input('Рост Бори: '))
height_v = float(input('Рост Вовы: '))
height_d = float(input('Рост Димы: '))

if height_b > height_v:
    if height_v > height_d:
        print(height_b)
        print(height_v)
        print(height_d)
    elif height_b > height_d:
        print(height_b)
        print(height_d)
        print(height_v)
    else:
        print(height_d)
        print(height_b)
        print(height_v)
else:
    if height_b > height_d:
        print(height_v)
        print(height_b)
        print(height_d)
    elif height_v > height_d:
        print(height_v)
        print(height_d)
        print(height_b)
    else:
        print(height_d)
        print(height_v)
        print(height_b)
