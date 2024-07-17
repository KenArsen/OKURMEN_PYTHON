# filter(func, *iterable)

cities = ['Bishkek', 'Naryn', 'Talas', 'Jalal-Abad']

def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

numbers = [2,3,4,5,6,7,8,9,11,13]
print(list(filter(is_prime, numbers)))


cities_filter = list(filter(lambda x: len(x) > 5, cities))
# print([i for i in cities if len(i) > 5])
print(cities_filter)