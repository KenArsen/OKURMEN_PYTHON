# 1 - Тапшырма
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

int_num1 = int(num1)
int_num2 = int(num2)

result_sum = int_num1 + int_num2

print("Эки сандын суммасы =", result_sum)


# 2 - Тапшырма
user_input = input("Enter some string: ")
print(user_input.upper())
print(user_input.lower())
print(user_input.title())

# 3 - Тапшырма
user_input = input("Enter some string: ")
print(user_input.isalpha())
print(user_input.isdigit())
print(user_input.isupper())

# 4 - Тапшырма
text = input("Введите строку: ")
search_word = input("Введите слово для поиска: ")
replace_word = input("Введите слово для замены: ")

result = text.replace(search_word, replace_word)

print(result)


# Кошумча тапшырма
date_of_birth = input("Enter date of birth (DD.MM.YYYY): ")
date = date_of_birth.split('.')
print(date_of_birth)
print(date)
day = date[0]
month = date[1]
year = date[2]
print(day)
print(month)
print(year)
print("Сиз", year, "жылдын", month, "айынын", day, "кунундо торолгонсуз")

