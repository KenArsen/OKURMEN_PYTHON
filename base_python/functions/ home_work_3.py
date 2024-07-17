# (name="Okurmen")  вот такие параметры называются -> формальными
# (a, b, c) а обычные –> фактическими

# 1 - тапшырма
"""
check_password деген функция жазыныздар,
ал биринчи параметр катары бир сап(строка), 
и экинчиге бир формальный параметр кабыл алат
ал по умолчанию барабар болсун '$%!?@#' ушул символдорго.
Функция текшериш керек, эгер жазылган парольдун 
ичинде ушул символдордун бири болсо жана узундугу 8 ден чон болсо
True болбосо False кайтарыш керек
"""

def check_password(password, simbols = '$%!?@#'):
    if len(password) > 8:
        for simbol in simbols:
            if simbol in password:
                return True
    return False

pas = input("Password: ")
print(check_password(password=pas))


# 2 - тапшырма
"""
get_rect_value еген функция жазыныздар,
ал озуно 2 параметр алсын(ширина, дилина)
анан дагы бир формальный параметр tp деген
болсун, по умолчанию ал True мааниге ээ.
Эгер tp барабар болсо True'га,
анда торт бурчтуктун периметрин,
болбосо аянтын чыграныздар
"""

def get_rect_value(a, b, tp=True):
    if tp == True:
        print((a + b) * 2)
    else:
        print(a * b)

get_rect_value(2, 3)
get_rect_value(3, 4, tp=False)