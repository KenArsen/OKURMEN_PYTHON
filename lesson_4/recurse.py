def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


f = fact(5)
print(f)
# 5! = 1*2*3*4*5