"""
3) Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите месяц года от 1 до 12: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Ошибка ввода!!! Такого месяца не существует")

"""
вариант преподавателя:
month = int(input("Введите номер месяца: "))

my_lst = [
    "Зима",
    "Зима",
    "Весна",
    "Весна",
    "Весна",
    "Лето",
    "Лето",
    "Лето",
    "Осень",
    "Осень",
    "Осень",
    "Зима"]
    
print(f'Результат через список: {my_lst[month - 1]}')

my_dict = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна",
           6: "Лето", 7: "Лето", 8: "Лето", 9: "Осень", 10: "Осень",
           11: "Осень", 12: "Зима"}
"""
