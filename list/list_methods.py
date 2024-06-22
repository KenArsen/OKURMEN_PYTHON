'''
.split()
.join()
Вывод с помощью цикла for
Вывод с помощью распаковки списка (*list_)

.insert()
.index()
.remove()
.pop()
.reverse()
.count()
.clear()
.sort()
.extend()

'''

# text = "Hello, how are you"
# text_list = text.split()
# print(text_list)

# # списоктун ар бир элементин биз берген параметер менен бириктирет
# new_text = "".join(text_list) 
# print(new_text)

# n = int(input())
# numbers = []
# for i in range(1, n+1):
#     numbers.append(str(i))
# print(numbers)
# print(",".join(numbers))


# nums = ['Arsen', [2,4,6], ['name', 'surname', ["hello"]]]
# #        0          1                2

# join_text = ''.join([nums[2][0], nums[2][1], nums[2][2][0]])
# print(join_text)

# print(nums[2])


# nums = ["Hello", 3, True, 3.45]
# for num in nums: 
#     print(num)
# print()

# message = "Good by, my brother, see you tommorow"
# print(*nums, sep='\n')
# print(*message, sep=',')


# numbers = [2,4,3,1,5]
# numbers.insert(17, "Ali")
# numbers.insert(20, "Okurmen")
# numbers.insert(15, 'Okurmen1')
# print(numbers)

# a = 3
# b = 2

# c = a
# a = b
# b = c

# a, b = b, a

# nums = ["Hello", 3.45, True, 3, True]

# ind = nums.index(3.45)
# nums[ind] = 4 # nums[3] = 4
# print(nums)
# nums[1], nums[3]=nums[3], nums[1]
# print(nums)
# x=0

# x=nums[1]
# nums[1]=nums[3]
# nums[3]=x
# print(nums)

# pop_element = nums[-1].pop(1)
# print(pop_element)
# print(nums)

# print(nums[::-1])
# nums.reverse()
# nums.sort()
# print(nums)

# nums = ["Hello", 3.45, True, 3, True]
# nums.append([23, 324, "Sister"])
# nums.extend([23, 324, "Sister"])
# print(nums)