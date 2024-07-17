cats = [
    ('Мартин', 5, 'Алексей', 'Егоров'),
    ('Фродо', 3, 'Анна', 'Самохина'),
    ('Вася', 4, 'Андрей', 'Белов'),
    ('Муся', 7, 'Игорь', 'Бероев'),
    ('Изольда', 2, 'Игорь', 'Бероев'),
    ('Снейп', 1, 'Марина', 'Апраксина'),
    ('Лютик', 4, 'Виталий', 'Соломин'),
    ('Снежок', 3, 'Марина', 'Апраксина'),
    ('Марта', 5, 'Сергей', 'Колесников'),
    ('Буся', 12, 'Алена', 'Федорова'),
    ('Джонни', 10, 'Игорь', 'Андропов'),
    ('Мурзик', 1,'Даниил', 'Невзоров'),
    ('Барсик', 2, 'Виталий', 'Соломин'),
    ('Рыжик', 7, 'Владимир', 'Медведев'),
    ('Матильда', 8, 'Андрей', 'Белов'),
    ('Гарфилд', 3, 'Александр', 'Березуев')
]

# numbers = map(int, input().split())

# list_numbers = list(numbers)
# set_numbers = set(list_numbers)

# print(list_numbers)
# print(set_numbers)
# dic = dict()
# for i in set_numbers:
#     s = 0
#     for j in list_numbers:
#         if i == j:
#             s = s + 1
#     dic[i] = s
# print(dic)

numbers_1 = map(int, input().split())
numbers_2 = map(int, input().split())

result = set(numbers_1) & set(numbers_2)
print(result)

print(list(numbers_1))
print(list(numbers_2))

