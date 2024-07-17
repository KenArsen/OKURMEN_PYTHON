# 1 - тапшырма
"""
эки сандын чонун тапкан lambda функция жазыныздар
"""
max_numbers = lambda a, b: a if a > b else b 
print(max_numbers(2, 3))


# 2 - тапшырма
"""
берилген тамганы ундуу же ундуу эмес экенин текшерген
lambda функция жазыныздар. Эгер тамга ундуу болсо
анда ла 'ундуу' болбосо 'ундуу эмес' деген жооп кайтарыш керек
"""
alphabet = lambda x: "ундуу" if x in 'aieyuo' else "ундуу эмес"
print(alphabet("b"))

# 3 - тапшырма
"""
Рекурсиянын жардамы менен 1 ден N ге чейинки сандардын
суммасын чыгарган функция жазыныздар
input:
5
output:
15
"""

def fun(n):
    if n == 1:
        return 1
    return fun(n-1) + n

num = int(input()) 

print(fun(num))