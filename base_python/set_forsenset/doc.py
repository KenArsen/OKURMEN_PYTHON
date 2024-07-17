# Создание .add()
# Пересечение &, 
# Удаление и очистка .clear(), .remove()
# Перебор элементов = for num in iterate_me:
# Сортировка множеств = in
# Сортировка множеств sorted(some_digits)
# Длина множества len()
# Операции на множествах
'''
lang_X = {'C++', 'Perl', 'PHP'}
lang_Y = {'Java', 'C#', 'PHP', 'Python'}
lang_Z = lang_X.union(lang_Y) # или так lang_Z = lang_X | lang_Y
print(lang_Z)
'''

# Пересечение
'''
unbreakable_diamond = ['Jotaro', 'Josuke', 'Koichi']
golden_wind = ['Jotaro', 'Koichi', 'Giorno']
# & - здесь оператор пересечения
overlap = set(unbreakable_diamond) & set(golden_wind)
print(overlap)
'''

#Разность множеств
'''
minuend = {23, 44, 1, 34, 98}
subtrahend = {23, 44, 1, 55, 76}
total = minuend.difference(subtrahend) # или так total = minuend - subtrahend
print(total)
> {34, 98}
'''


# lang_X = {'C++', 'Perl', 'PHP'}
# lang_Y = {'Java', 'C#', 'PHP', 'Python'}
# minuend = {23, 44, 1, 34, 98}
# print(sorted(minuend))
# print(len(minuend))



# lang_Z = set(lang_X) & set(lang_Y) 
# print(lang_Z)

# for lang in lang_Y:
#     print(lang)

# print(lang_Y)
# lang_Y.remove("Java")
# print(lang_Y)


minuend = {23, 44, 1, 34, 98}
subtrahend = {23, 44, 1, 55, 76}
total_A = minuend.difference(subtrahend)
total_B = subtrahend.difference(minuend)
symmetric_d = minuend.symmetric_difference(subtrahend)

print(total_A)
print(total_B)
print(symmetric_d)


it = {'green', 'white', 'red'}
it_sub = {"green", "white"}
ru = {'white', 'blue', 'red'}
ukr = {'blue', 'yellow'}


print(ukr.isdisjoint(ru))
print(it_sub.issubset(it))
print(it_sub.issuperset(it))
ru.add("yellow")
print(ru)

ru = frozenset(ru)