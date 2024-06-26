# 1 - тапшырма
"""
Функция жазыныздар, анын аты is_triangle болсун
жана ал озуно 3 параметр алсын(уч бурчтуктун уч жагы),
текшериш керек ошол берилген уч сан менен уч бурчтук
тузууго болобу. Эгер болос функция True деген болбосо False
деген жооп кайтарыш керек

Мисалы:
is_triangle(3, 6, 10) бизге кайтарыш керек False
is_triangle(3, 6, 8) бизге кайтарыш керек True
"""

def is_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    return False

print(is_triangle(3, 5, 3))


# 2 - тапшырма
"""
Функция жазыныздар, анын аты is_large болсун
жана ал озуно 1 параметр алсын(текст),
текшериш керек ошол берилген тексттин узундугу учтон
чон болсо функция True деген болбосо False
деген жооп кайтарыш керек

Мисалы:
is_large("I love Python!") бизге кайтарыш керек True
is_large("Hi") бизге кайтарыш керек False
"""

def is_large(text):
    return len(text) > 3     

print(is_large("I love Python!"))    


# 3 - тапшырма
"""
Бир функция жазыныздар, анын бир параметри болот(ал сан int болуш керек)
функция текшериш керек эгер берилген сан жуп болсо True
болбосо False кайтарыш керек

Санды консольдон алып, аны функцияга аргумент катары бериниздер


Мисалы:
5 деген сан берсек функция кайтарыш керек False
6 деген сан берсек функция кайтарыш керек True
"""

def is_jup(number):
    return number % 2 == 0

print(is_jup(6))

# 4 - тапшырма
"""
Бир функция жазыныздар, анын бир параметри болот(ал список list болуш керек)
функция бизге эн чон сан менен эн кичине сандын 
суммасын жана айырмасын кайтарыш керек

Списокту консольдон алып, аны функцияга аргумент катары бериниздер


Мисалы:
19 10 23 34 14 5 15  деген списко берсек 
функция кайтарыш керек 39(34 + 5) жана 29(34 - 5)
"""

def get_sum_max_min_element(numbers):
    max_element = numbers[0]
    min_element = numbers[0]
    for number in numbers:
        if number > max_element:
            max_element = number
        if number < min_element:
            min_element = number
    print(max_element + min_element)
    print(max_element - min_element)

get_sum_max_min_element([1,2,3,4,5])