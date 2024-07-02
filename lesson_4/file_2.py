# def get_list(a, b, d, *args):
#     print(a)
#     print(b)
#     print(args)
#     print(d)

# get_list(1,2,3)

# def get_all(a, b, c, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(kwargs)


# get_all(1, 2, 3, arsen="Arsen", ali="Ali")
# get_all(a=1, b=2, c=3, d=6, e=5)

# def list1(*args, **kwargs):
#     print(*args)
#     print(kwargs['a'])
#     print(kwargs['b'])
#     print(kwargs['c'])

# list1(1,2,3,4, a=3, b=4, e=5, c=True)


# 2 3 4 5 6 7 8
# a = 2
# b = 3
# c = 4 5 6
# d = 7
# e = 8

# def get_numbers(a, b, d, e, *c):
#     print(f'a = {a}')
#     print(f'b = {b}')
#     print(f'c = {c}')
#     print(f'd = {d}')
#     print(f'e = {e}')


# a, b, *c, d, e = [i for i in input().split()]
# get_numbers(a, b, d, e, *c)


# Arsen Kenzhegulov 22

{"name": "Arsen", "surname": "Kenzhegulov", "age": "22"}

def get_person(**kwargs):
    # a = kwargs['name']
    # b = kwargs["surname"]
    # c = kwargs["age"]
    # print(f'Name: {a}')
    # print(f'Surname: {b}')
    # print(f'Age: {c}')

    for key, value in kwargs.items():
        print(key, value, end='; ')

name, surname, age = [i for i in input().split()]
get_person(name=name, surname=surname, age=age)

