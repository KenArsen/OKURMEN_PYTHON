num_1 = int(input("Enter number one: ")) 
num_2 = int(input("Enter number two: "))
num_3 = int(input("Enter number three: "))

big_number = (num_1 + num_2) ** num_3
# big_number = (12 + 21) ** 1

print(big_number)
tak_sandar = 0

if big_number % 2 == 1:
    tak_sandar = big_number // 2 + 1
else:
    tak_sandar = big_number // 2

print(tak_sandar)








# tak_sandaryn_sany = 0 

# if num_1 % 2 == 1: # 3 % 2 == 1 , 1 == 1
#     tak_sandaryn_sany = tak_sandaryn_sany + 1 # 0 + 1 = 1

# if num_2 % 2 == 1: # 2 % 2 == 1, 0 == 1
#     tak_sandaryn_sany = tak_sandaryn_sany + 1 # 

# if num_3 % 2 == 1: # 1 == 1
#     tak_sandaryn_sany = tak_sandaryn_sany + 1 # 1 + 1 = 2


# print("Tak sandardyn sany = ", tak_sandaryn_sany)