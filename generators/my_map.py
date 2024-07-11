# map(func, *iterable)

# a, b, c = map(int, input().split())

def get_tak(number):
    return number % 2 == 1

numbers_bool = map(get_tak, range(10))
# 0 1 2 3 4 5 6 7 8 9
print(numbers_bool)
print(list(numbers_bool))


cities = ['Bishkek', 'Naryn', 'Talas', 'Jalal-Abad']

cities_upper = list(map(lambda x: x.upper(), cities))
print(cities_upper)
