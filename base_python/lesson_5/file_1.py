# def recursive(value):
#     if value > 4:
#         return value
#     print(value) 
#     return value + recursive(value + 1)

# # 0 + 15
# # 1 + 14
# # 2 + 12
# # 3 + 9
# # 4 + 5
# # 5


# print(recursive(0))
# # 0
# # 1
# # 2
# # 3
# # 4


# def Rec(n):
#     print(n)
#     if n == 0:
#         return 0
#     return n + Rec(n-1)
# #          3 + 3
# #          2 + 1
# #          1 + 0
# #          0

# print(Rec(0))
# 1 1 2 3 5 8 13 21 34 55


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))