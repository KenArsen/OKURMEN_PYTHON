# numbers = input("Сандарды киргизиңиз (боштук менен бөлүп): ").split()

# numbers = [int(number) for number in numbers]

# sum_of_numbers = sum(numbers)

# print("Бардык сандардын суммасы:", sum_of_numbers)



print("Сандарды киргизиңиз (боштук менен бөлүп):", end=" ")

numbers = [int(number) for number in input().split()]

sum_of_numbers = 0
for number in numbers:
    sum_of_numbers += number

print("Бардык сандардын суммасы:", sum_of_numbers)
