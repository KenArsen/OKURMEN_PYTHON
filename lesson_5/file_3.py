# name = "Okurmen"
# city = "Bishkek"

# def fun():
#     age = 2
#     print(age)
#     name = "Booster"
#     print(name)

#     def sub_fun():
#         name = "Hello"
#         print(name)
#         print(city)
    
#     sub_fun()
#     print(name)
#     print(city)



# fun()
# print(name)


# surname = "Asanov"

# def test():
#     global surname
#     surname = "Usonv"

# test()
# print(surname)


# I study in okurmen
# I study in BOOSTER

# My name is okurmen
# My name is BOOSTER

change = lambda text, old, new: text.replace(old, new)
list_1 = lambda x: [i for i in range(x)] if x > 5 else False
print(list_1(6))

text = input("text: ")
old = input('old: ')
new = input("new: ")
print(change(text=text, old=old, new=new))


