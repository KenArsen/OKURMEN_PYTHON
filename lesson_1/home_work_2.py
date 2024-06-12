fist_name = input("Enter your name: ")
last_name = input("Enter your surname: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ") 
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

'''
Жогорудагы озгормолорго биз маанилерди консольдон киризебиз

Мисалы:

    first_name = Arsen
    last_name = Kenzhegulov
    phone = 0706484681
    email = examle@gmail.com
    age = 22
    height = 1.82
    weight = 60

1) Жооп катары консольго томондогудой болуп чыгышы керек
    Name: Arsen Kenzhegulov
    Phone: 0706484681
    Email: examle@gmail.com
    Age: 22 jash
    Height: 1.82 m
    Weight: 60 kg

2) Берилген жашы боюнча анын кайсы категорияга кирерин аныкташыбыз керек
    Эгерде 0 <= age <= 18 анда жоопко (You are a child.)
    Эгерде 13 <= age <= 19 анда жоопко (You are a teenager.)
    Эгерде 20 <= age <= 64 анда жоопко (You are an adult)
    Эгерде 65 > age анда жоопко (You are a senior)

    буларды if, elif, else шарттуу операторлорун колдонуп чагарыныздар

Кошумча тапшырма, эгер убактыныз болсо

Body Mass Index (BMI)(Дене салмагынын индекси)
Дене массасынын индекси - бул адамдын салмагы менен боюнун ортосундагы 
дал келүү даражасын баалоого жана ошону менен салмактын жетишсиз, 
нормалдуу же ашыкча экендигин аныктоочу программа.

Формуласы -> BMI = weight / (height ** 2)
Салмагын боюнун узундугунун экинчи даражасына болгонго барабар
Эгерде bmi < 18.5 болсо, жоопка (Underweight) чыгышы керек
Эгерде 18.5 <= bmi < 24.9 болсо, жоопко (Normal weight) чыгышы керек
Эгерде 25 <= bmi < 29.9 болсоб жоопко (Overweight) чыгышы керек
'''
