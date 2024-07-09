# 1 - тапшырма 
"""
Консольдон float тибиндеги сан берилет. 
Бул санды окуп, math модулун импорттоо керек, 
окулган сан үчүн math.ceil функциясын чакырып, 
натыйжасын экранга чыгаруу керек.

Мисал:
5.67
Жооп:
6
"""

# import math
from math import ceil
n = float(input("Введите одно число: "))
# print(math.ceil(n))
print(ceil(n))


# 2 - тапшырма 
"""
Программага random модулунан seed жана randint функцияларын гана импорттоо керек. 
Андан кийин, бул функцияларды төмөнкүдөй аткарыңыз:

seed(1)
print(randint(10, 50))
"""

from random import randint, seed
seed(1)
print(randint(10, 50))
