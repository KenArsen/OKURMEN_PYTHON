a = [1, 2, "Naryn", lambda a, b: print(a+b), 'Bro', True]
print(a)
print(a[3])
print(a[3](2, 3))


def get_filter(lst, filter=None):
    if filter is None:
        return lst
    res = []
    for x in lst:
        if filter(x):
            res.append(x)
        
    return res

a = [1,2,3,4,5]
b = get_filter(lst=a)
c = get_filter(lst=a, filter=lambda x: x % 2 == 0)
print(b)
print(c)

