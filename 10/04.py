n = int(input())
text_l = []
for i in range(n):
    text_l += [input()]
print(*sorted(text_l, key=len), sep='\n')
