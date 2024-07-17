'''
if шарт :
    блок кода
elif шарт :
    блок кода
else:
    блок кода

'''


age = 10 
if age == 10:
    print("Sidin jashynyz 10do")
if age == 11: # False
    print()
if age > 18:
    print("if ishtedi")
    print(age)
    age = age - 7 # 18
    print(age)
    # 25
    # 18
elif age < 18:
    print("Elif ishtedi")

age_1 = 20
age_2 = 40
if age_1 > 18 and age_2 < 50 and age_1 < age_2: # True True True -> 1 * 1 * 1 = 1
    print("alkjdf")
if age_1 < 18 and age_2 < 50: # False -> 0
    print()
if age_1 > 10 or age_2 < 50:
    print()


name = "Okurmen"
age = 1
if age > 2 or not name == "Okurmen" and age != 1: # False + False * True
    print("if ishtedi")
else:
    print("else ishtedi")
