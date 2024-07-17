n, m = map(int, input().split())

numbers = [
    [int(i) for i in input().split()]
    for j in range(n)
]

res_max = []
res_min = []
for i in range(n): # 0, 1
    res_max.append(max(numbers[i]))
    res_min.append(min(numbers[i]))
print(*res_max)
print(*res_min)
# 123456789
# 123455678

