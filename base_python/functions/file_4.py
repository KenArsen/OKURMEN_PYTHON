"""
def <функциянын аты>(параметрлер):
    operator_1
    operator_2
    .
    .
    .
    operator_n

    return 

send_mail(аргмутенттер)
""" 

def sum_a_b(a, b):
    result = a + b # 10
    print(result)
    return result 


def get_info():
    name = "Arsen"
    surname = "Kenzhegulov"
    people = ["Arnas", "Argen", "Asan"]
    return name, surname, people


def set_name(name):
    name_1 = name
    return name_1
    

res = sum_a_b(3, 7)
a, b, c = get_info()
set_n = set_name("Okurmen")
print(res)
print(a)
print(b)
print(c)
print(set_n)
a_b_sum = sum_a_b
print(a_b_sum(3,4))
