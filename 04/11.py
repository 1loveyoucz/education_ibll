people = int(input())
iq_sum = 0
for i in range(people):
    iq = int(input())
    iq_sum += iq
    sr_zn = iq_sum / (i+1)

    if iq == sr_zn:
        print(0)
    elif iq > sr_zn:
        print('>')
    else:
        print('<')
