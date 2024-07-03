# lambda

# lambda para_1, para_2, ... para_n: command

# a = lambda x, y: x + y

# print(a(3, 4))

# b = lambda number: number % 2 == 0

# print(b(6))


a = lambda name: f'{name} - {len(name)}'
for i in ["Kyrgyzstan", "Kazakstan", "Uzbekstan"]:
    print(a(name=i))

sqrt_fun = lambda x: x ** 0.5

print(sqrt_fun(5))
print(sqrt_fun(102))

