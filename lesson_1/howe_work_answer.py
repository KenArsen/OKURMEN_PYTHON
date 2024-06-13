fist_name = input("Enter your name: ")
last_name = input("Enter your surname: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ") 
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))


# 1 - Тапшырма
print("Info about you")
print("Name:", fist_name, last_name)
print("Phone:", phone)
print("Email:", email)
print("Age:", age)
print("Height:", height)
print("Weight:", weight)

# 2 - Тапшырма
print("\n")
if 0 <= age <= 18:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif 20 <= age <= 64:
    print("You are an adult")
else:
    print("You are a senior")


# Кошумча тапшырма
print("\nYour BMI", end=' - ')
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight") 
