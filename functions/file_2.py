def max_a_b_c(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
def get_max_element(numbers):
    max_element = 0
    for number in numbers:
        if number > max_element:
            max_element = number
    print(max_element)


def get_min_element(numbers):
    min_element = 100
    for number in numbers:
        if number < min_element:
            min_element = number
    print(min_element)

    

# print(max_a_b_c(58, 56, 98))
# numbers = [58, 65, 41, 25, 68, 79]
get_max_element([58, 65, 41, 25, 68, 79])
get_min_element([58, 65, 41, 25, 68, 79])
