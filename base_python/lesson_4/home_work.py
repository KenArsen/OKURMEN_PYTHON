# 1 - тапшырма
"""
Функция жазыныздар ал параметр катары бир  *args алсын,
функция бизге кайтарып берсин бир гана жуп санадарды.
Сандарды биз озубуз консольдон киргизебиз!
Функциянын аты get_even босун!
"""

def get_even(*args):
    result = []
    for number in args:
        if number % 2 == 0:
            result.append(number)
    return result

numbers = [int(i) for i in input().split()]
print(get_even(1,2,3,4,5))
print(get_even(*numbers))



# 2 - тапшырма
"""
Функция жазыныздар ал параметр катары бир  *args алсын,
функцияга биз аргумент катары шаардын аттарын беребиз.
Функция кайтарып бериш керек, аты эн узун шаар атын,
эгерде узундугу бирдей болгон шаарлар бир нече болсо,
анда эн биринчи берилген шаарды чыгарыныздар!
Функциянын аты get_biggest_city болсун!
Мисалы:
Bishkek Osh Talas Batken Stambul
Жоопко:
Bishkek
"""

def get_biggest_city(*args):
    max_len = len(args[0])
    max_city = args[0]
    for city in args:
        if len(city) > max_len:
            max_len = len(city)
            max_city = city
    return max_city


print(get_biggest_city("Bishkek", "Osh", "Talas", "Batken", "Jalal-Abad"))