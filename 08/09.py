n = int(input())
codes_l = ''
for i in range(n):
    codes = input()
    if '####' in codes[:5]:
        codes_l += "\n"
    elif '%%' in codes[:3]:
        codes_l += codes[2:] + '\n'
    else:
        codes_l += codes + '\n'
print(codes_l)
