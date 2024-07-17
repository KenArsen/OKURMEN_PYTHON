# while 
# while шарт:
    # биз жазган шарт качан False маани кайтармайынча иштейт
    # биз жазган шарт качан аткарылбай калганча иштейт

i = 0
while i <= 10: # True False
    print(i) # 0 1 2 3 4 5 6 7 8 9 10
    i += 1

message = ""
while message != 'Okurmen': # True False
    print(message) # ""
    message = "Okurmen"
    print(message) # Okurmen



# 1,...,20 
a=0
b=0 
c=int(input())
for  i in range (c):
    if i%2==1:
        a=a+i
    else:
        b=b+i

print(a)
print(b)


