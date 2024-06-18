# # range(башы, аягы, кадамы)
# # range(10) -> 0,1,2,3,4,5,6,7,8,9
# # range(5, 10) -> 5,6,7,8,9
# # range(4, 10, 2) -> 4,6,8

# # for
# # for озгормо in range()

# # for i in range(5):
# #     # i = 0
# #     # i = 1
# #     # i = 2
# #     # i = 3
# #     # i = 4
# #     print("index = ", i)

# # message = "Hello, my bro. My name is Okurmen" 

# # for alphabet in message:
# #     print(alphabet)

# text = "Век живи - век учись."

# first_part = ""
# print("first part =", text[:8])
# for i in text[:8]:
#     # i = В 
#     # i = е 
#     # i = к 
#     # i =  
#     # i = ж 
#     # i = и 
#     # i = в 
#     # i = и 
#     first_part = first_part + i # first_part = Век живи

# second_part = ""
# print("second part: ", text[11:-1])
# for i in text[11:-1]:
#     # i = в
#     # i = е
#     # i = к
#     # i = 
#     # i = у
#     # i = ч
#     # i = и
#     # i = с
#     # i = ь
#     second_part = second_part + i # second_part = век учись

# print(second_part + " - " + first_part)

# # 1,2,3,4,5...,20
# # 2,4,6,8,10,12,14,16,18,20
# # 1,3,5,7,9,11,13,15,17,19
# # jup sandardyn summasy = 110
# tak sandardyn summasy = 100

sumJ = 0
sumT = 0
for i in range(21):
    if i % 2 == 0:
        sumJ += i # sumJ = 110
    else:
        sumT += i # sumT = 100
print("tak sandardyn summasy:", sumT)
print("jup sandardyn summasy: " , sumJ)

if sumJ > sumT:
    print("Jup sandardyn summasy chon")
else:
    print("Tak sandardyn summasy chon")