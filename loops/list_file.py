# numbers_1 = []
# numbers_2 = list()

# people = ["Aizhan", "Hadicha", "Amantur", "Ali", "Akbar"]

# length = len(people)

# for person in people:
#     if len(person) < 5:
#         print(person)

# numbers = [23,21,45,53,52,62,76,89,91,110]
# jup_numbers = []
# tak_numbers = []

# for number in numbers:
#     if number % 2 == 1:
#         tak_numbers.append(number)
#     else:
#         jup_numbers.append(number)

# print(tak_numbers)
# print(jup_numbers)
# print(..., end=" ")


# people = ["Aizhan", "Hadicha", "Amantur", "Ali", "Akbar"]

# for i in range(len(people)):
#     if people[i] == 'Ali':
#         people[i] = 'Arsen'
# print(people)
# people.append("Aizhan")

# people.remove("Arsen")
# l = people.count("Aizhan")
# print(people)

people = []

while True:
    name = input("Enter name: ")
    if name == "":
        break

    people.append(name)

    for person in people:
        print(person, "=", people.count(person))
    