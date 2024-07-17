# 1 - Тапшырма
'''
Бизге n деген сан берилет консольдон,
консольго чыгарыш керек n*n форматындагы массивди 
ар бир индекстин квадыратын.
Мисалы:
n = 3
1  4  9
16 25 36
49 64 81
ушинтип чыгыш керек
'''

# n = int(input("Enter a number: "))
# s = 0
# for i in range(n):
#     for j in range(n):
#         s += 1
#         print(s ** 2, end=" ")
#     print()


# 2 - Тапшырма
'''
Фибоначчи сандары
0,1,1,2,3,5,8,13,21,34,55,...
мында биринчи эки сан (0 мене 1) 
жана ар бир кийинки сан мурунку 
эки сандын суммасына барабар болот.

Бизге n деген сан берилет консольдон,
жоопко n чи Фибоначчи санын чыгарыныз.
Мисалы:
n = 7
Жетинчи Фибоначчи саны 8 барабар болгондуктан
жоопко 8 деп чыгыш керек
'''

n = int(input("Enter a number: "))
value_1 = 0
value_2 = 1
if n <= 0:
    print("Enter a number > 0, please!")
elif n == 1:
    print(value_1)
elif n == 2:
    print(value_2)
else:
    for i in range(2, n):
        current_value = value_1 + value_2
        value_1 = value_2
        value_2 = current_value
    print(current_value) 
