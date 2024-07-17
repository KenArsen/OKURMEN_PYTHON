int_number = 20
float_number = 12.34

result_sum = int_number + float_number
print(result_sum)

str_number = "22"
str_to_int_number = int(str_number) # 22
str_to_float_number = float(str_number) # 22.0

print(int_number + str_to_int_number)
print(int_number + str_to_float_number)

# False = 0
# True = 1
print(int(True)) # 1
print(int(False)) # 0
print(float(True)) # 1.0
print(float(False)) # 0.0

# # str_text = str(int_number)  
# print(str_text) # 22
# print(type(str_text)) # 22 type <str>

comment = "Hello, my bro" + str(int_number)
print(comment)

# str(), int(), float()

a = 20 
b = "1234" # int
c = 'message' # int
d = 12.4 # float -> str
print(type(c))
result = str(c)
print(result)
print(type(result))
