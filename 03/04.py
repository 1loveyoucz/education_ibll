str_list = []
str_1 = str(input())
while str_1 > '':
    str_list += [str_1]
    str_1 = str(input())
for element in str_list:
    print(element)
