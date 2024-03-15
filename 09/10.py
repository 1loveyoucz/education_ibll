n = int(input())
numb_l = []
for i in range(n):
    numb = int(input())
    numb_l += [numb]
p = int(input())
q = int(input())
answer = 0
for j in range(p-1,q):
    answer += numb_l[j]
print(answer)