# fibonacci -> 0 1 1 2 3 5 8 ...
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fib(n-1) + fib(n-2)

# print(fib(4))

def rec(x): 
    if (x < 4):
        print(x) # 1 2 3 3 2 1
        rec(x + 1)
        print(x)

# rec(1)
    

# заказ
def palindrom(s):
    # котяток
    # отято
    # тят
    # я
    if len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])

print(palindrom("котяток"))
s = "котятос"
print(s == s[::-1])

