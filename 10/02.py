n = int(input("Введите количество школьников: "))
students_l = []
for i in range(n):
    students = input()
    students_l.append(students)
for student in students_l:
    print(student)
print()
for student in students_l:
    if '4' in student or '5' in student:
        print(student)