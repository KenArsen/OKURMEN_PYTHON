from datetime import datetime

a = [1, 2, 3]
b = [4, 5, 6, 7, 8, 9]
c = [11, 12]
print(list(zip(a, b, c)))

names = ["Arsen", "Ali", "Amantur"]
surnames = ["Kenzhegulov", "Turganbaev", "Nurlanbekuulu"]

print(tuple(zip(names, surnames)))
print(dict(zip(names, surnames)))

# 2 5
# 2 3 4 5
# 4 9 16 25

a, b = map(int, input().split())
print(tuple(map(lambda x: x ** 2, [i for i in range(a, b + 1)])))
# здесь продолжайте программу


def get_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print(end_time - start_time)
    return wrapper

def my_map(nums):
    list(map(lambda x: x ** 2, nums))

def my_list(nums):
    return [i ** 2 for i in nums]

n = list(range(1, 10000))
my_map = get_time(func=my_map)
my_map(nums=n)
my_list = get_time(func=my_list)
my_list(nums=n)



