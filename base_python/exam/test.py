# 1-тапшырма
# message = "Pyhton is cool"
# print(message[::-1])

# 2-тапшырма
# tak_sandar = [san for san in range(1, 20)if san % 2 == 1]
# jup_sandar = [san for san in range(1, 20)if san % 2 == 0]
# print(tak_sandar)
# print(jup_sandar)

numbers_ahd_letters = input()
a = []
for i in numbers_ahd_letters:
    if i.isdigit():
        a.append(int(i))
    else:
        a.append(int(i))
print(a)
# 3-тапшырма
number = [1,2,3,...,n]
jup_numbers = []
tak_numbers = []
for number in number:
    if number % 2 ==1:
        tak_numbers.append(number)
    else:
        jup_numbers.append(number)