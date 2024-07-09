from random import randint

def set_number():
    return randint(1, 10)

def check(computer, value):
    return computer == value

def set_range(start, end):
    return randint(start, end)

def start(is_range=False):
    i = 0
    if is_range:
        n, m = map(int, input("Введите два число через пробел: ").split())
    comp = set_range(start=n, end=m) if is_range else set_number()
    while True:
        n = int(input("Введите ваше число: "))
        i += 1

        is_true = check(computer=comp, value=n)

        if is_true:
            print("Siz sandy taptynyz!")
            break
        else:
            if i < 3:
                print("Dagy araket kylynyz")
            else:
                print("Siz utuldunuz!")
                print(f"Computer oilogon san = {comp}")
                break