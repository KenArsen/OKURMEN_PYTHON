# 1 - Тапшырма
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')

# 2 - Тапшырма
number = int(input("Enter a number: "))
if number > 2:
    for i in range(1, number + 1):
        print('*' * i)
else:
    print("2 ден чон сан жазыныз!")