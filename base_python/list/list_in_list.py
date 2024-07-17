n = int(input("Enter a number: "))
s = 0
s=n*n
for i in range(n): 
    for j in range(n):
        print(f'{s:<3}', end=" ")
        s-=1
    print() # \n 

# 3
# 9 8 7
# 6 5 4
# 3 2 1


# n = 3
# i = 0
    # j = 0
        # s = 1
    # j = 1
        # s = 2
    # j = 2
        # s = 3
# i = 1
    # j = 0
        # s = 4
    # j = 1
        # s = 5
    # j = 2
        # s = 6
# i = 2
    # j = 0
        # s = 7
    # j = 1
        # s = 8
    # j = 2
        # s = 9 
