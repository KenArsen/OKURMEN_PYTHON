def max_a_b(a, b):
    return a if a > b else b


def max_a_b_c(a, b, c):
    # a = 10, b = 11, c = 12
    k = max_a_b(a, b) # 11
    return k if c < k else c

print(max_a_b(10, 11))
print(max_a_b_c(10, 11, 12))
print(max_a_b(15, max_a_b(18, 17)))