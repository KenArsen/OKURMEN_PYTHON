"""
bool -> True, False
int -> -27439 ... 8073294
float -> 2.13, 3.98530, 3.90234
str -> 'adjf', '1jfdk', 'dfjl'
"""

name = "Erbol" # str
age = 25 # int
is_married = True # bool
height = 184 # int
weight = 85.5 # float
address = 'Bishkek, Turusbekov 109/1' # str

print(type(name))
print(type(age))
print(type(is_married))
print(type(height))
print(type(weight))
print(type(address))

"""
Erbol -> (class, 'str')
age -> int
"""

print(name, ' = ', type(name))
print(age, ' = ', type(age))
print(is_married, '<>', type(is_married))

