# a = {}
# a = dict()

a = {}
print(type(a))
a = dict()
print(type(a))

# key : value
# ключ : значение

cities = {
    "Bishek": "01",
    "Osh": "02",
    "Batken": "03",
} 
digits = {
    "One": 1,
    "Two": 2,
    "Three": 3,
}

# print(digits['One'])
# print(digits["Two"])
# print(digits["Three"])
# print(digits.get("Four"))
# print(digits.keys())
# print(digits.values())
# print(digits)
# digits["Four"] = 5
# print(digits)
# digits["Four"] = 4
# print(digits)

# print(digits["Two"] + digits["Four"])

# users_list = [
#     ["+958758767", "Alice"]
#     ]

# users_tuple = (
#     ("+111123455", "Tom"),
#     ("+384767557", "Bob"),
#     ("+958758767", "Alice")
# )


# users_dict = dict(users_list)
# users_tuple_dict = dict(users_tuple)
# print(users_dict)
# print(users_tuple_dict)

# # users_tuple[0] = ("+384767557", "Bek"),
# users_tuple_dict["+111123455"] = "Tonia"
# print(users_tuple_dict)



cities = {
    "Bishek": "01",
    "Osh": "02",
    "Batken": "03",
} 
digits = {
    "One": 1,
    "Two": 2,
    "Three": 3,
}

for key, value in digits.items(): 
    if key == "One":
        digits[key] = "one"


print(digits)