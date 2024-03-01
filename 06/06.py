books_1 = int(input('Число книг в домашней библиотеке: '))
books_2 = int(input('Число книг в списке на лето: : '))
books_library = set()
books_summer = set()
print('Книги в домашней библиотеке')
for i in range(books_1):
    book = input()
    books_library.add(book)
print('Книги на лето')
for j in range(books_2):
    book = input()
    books_summer.add(book)
b_double = books_summer & books_library
for c in b_double:
    print('YES')
else:
    print('NO')