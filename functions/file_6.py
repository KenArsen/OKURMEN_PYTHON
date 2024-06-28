def area(width, height):
    return width * height

# print(area(4, 3))

def get_sqrt(n):
    return n ** (1/2)
    # return n ** 0.5

# number = int(input("Enter a number: "))
# print(get_sqrt(number))


def get_list(nums):
    for num in nums:
        print(num, end=', ')
    print()


def get_max_element(nums):
    max_element = int(nums[0])
    for num in nums:
        if int(num) > max_element:
            max_element = int(num)
    return max_element


def get_sum_list(nums):
    total_sum = 0
    for num in nums:
        total_sum += int(num)
    print(total_sum)



numbers = [i for i in input().split()]
print(numbers)
m_element = get_max_element(numbers)
get_sum_list(numbers)
print(m_element)
