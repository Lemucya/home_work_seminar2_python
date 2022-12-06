"""
4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
my_string = input("Введите предложение: ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word[element]}")
        number += 1
    else:
        print(f" {number} {my_word[element][0:10]}")
        number += 1

"""
вариант преподавателя:
my_lst = input("Введите слова через пробел: ").split()
n = 1
for elem in my_lst:
    if len(elem) > 10:
        print(f"{n}. {elem}")
    n += 1
    
print()

for i, el in enumerate(my_lst, 1):
    print(f'{i}. {el[:10]}')
"""