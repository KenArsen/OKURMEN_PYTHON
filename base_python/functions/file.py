def get_tak_sandar(numbers):
    result = []
    for number in numbers:
        if number % 2 == 1:
            result.append(number)
    return result

tak_sandar = get_tak_sandar([1,2,3,4,5,6,7,8,9])
tak_sandar_2 = get_tak_sandar([8, 12, 23, 54, 78])
print(tak_sandar)
print(tak_sandar_2)