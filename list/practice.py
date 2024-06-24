# score = {
#     1: 'AEIOULNSTR',
#     2: 'DG',
#     3: 'BCMP',
#     4: 'FHVWY',
#     5: 'K',
#     8: 'JX',
#     10: 'QZ'
# }

# word = input()
# word = word.upper()

# total_score = 0
# for letter in word:
#     for key, value in score.items():
#         if letter in value:
#             total_score += key
#             break
# print(total_score)

# cats = [
#     ('Мартин', 5, 'Алексей', 'Егоров'),
#     ('Фродо', 3, 'Анна', 'Самохина'),
#     ('Вася', 4, 'Андрей', 'Белов'),
#     ('Муся', 7, 'Игорь', 'Бероев'),
#     ('Изольда', 2, 'Игорь', 'Бероев'),
#     ('Снейп', 1, 'Марина', 'Апраксина'),
#     ('Лютик', 4, 'Виталий', 'Соломин'),
#     ('Снежок', 3, 'Марина', 'Апраксина'),
#     ('Марта', 5, 'Сергей', 'Колесников'),
#     ('Буся', 12, 'Алена', 'Федорова'),
#     ('Джонни', 10, 'Игорь', 'Андропов'),
#     ('Мурзик', 1,'Даниил', 'Невзоров'),
#     ('Барсик', 2, 'Виталий', 'Соломин'),
#     ('Рыжик', 7, 'Владимир', 'Медведев'),
#     ('Матильда', 8, 'Андрей', 'Белов'),
#     ('Гарфилд', 3, 'Александр', 'Березуев')
# ]
# # "Игорь Андропов": ["Джонни, 10", "Муся, 7"]

# result = {}
# for cat in cats:
#     value = cat[0] + ", " + str(cat[1])
#     result.setdefault(cat[2:], []).append(value)
#     # setdefault(key, defult)

# for key, value in result.items():
#     print(f'{key}: {value}')


text = input() # Okurmenokur - > okurmenokur
{
    "o": 2,
    "k": 2,
    "u": 2,
    "r": 2,
    "m": 1,
    "e": 1,
    "n": 1,
}

result = {}
text = text.lower()
for letter in text:
    result[letter] = text.count(letter)
    

print(result)
    

names = ["Arsen", "Bakbol", "Erbol", "Bekzhan"]
surnames = ["Kenzhegulov", "Shirgeliev", "Shirgeliev", "Kudakeev"]

{
    "Arsen": "Kenzhegulov",
    "Bakbol": "Shirgeliev",
    "Erbol": "Shirgeliev",
    "Bekzhan": "Kudakeev",

}

length = len(names)
people = dict()
for i in range(length):
    people[names[i]] = surnames[i]
print(people)
for key,value in people.items():
    print(key,value)
    

