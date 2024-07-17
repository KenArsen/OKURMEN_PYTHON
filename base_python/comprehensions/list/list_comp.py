# a = []
# for i in range(1, 10):
#     a.append(i ** 2)
# print(a)


# b = [i ** 2 for i in range(1, 10)]
# print(b)

# str_number = '2109438'
# int_number = []
# for i in str_number:
#     int_number.append(int(i))
# print(int_number)

# int_number = [int(i) for i in str_number]
# print(int_number)


# tak_sandar = [san for san in range(1, 20) if san % 2 == 1]
# jup_sandar = [san for san in range(1, 20) if san % 2 == 0]
# print(tak_sandar)
# print(jup_sandar)

# message = "I love Kyrgyzstan"
# x=message.split()
# print(x)
# s=[len(i) for i in x]
# print(s)

# print([len(i) for i in "I love Kyrgyzstan".split()])


# numbers = [int(i) for i in input().split()]
# print(numbers)

# t = [int(i) if i.isdigit() else str(i) for i in input().split()]
# print(t)

# numbers_and_letters = input()
# a = []
# for i in numbers_and_letters:
#     if i.isdigit():
#         a.append(int(i))
#     else:
#         a.append(str(i))
# print(a)

# 2 3 8 5 3 5 9 8 1
# [4, 27, 64, 125, 27, 125, 729, 64, 1]

result = [
    int(i) ** 2 if int(i) % 2 == 0 else int(i) ** 3  
    for i in input().split()
    ]
print(type(result))
result.append(23)
print(result)

types = [type(i) for i in input().split()]
print(types)