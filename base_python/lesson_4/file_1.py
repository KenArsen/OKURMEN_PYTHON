from base_python.lesson_4.file_2 import get_person
print(get_person(name="arsen"))

def test(a, b, c, d):
    print(a, b, c, d)

test(1, 2, 3, 4) 
test(d=1, a=2, c=3, b=4)

def test_1(a, b, c=3):
    print(a, b, c)

test_1(a=3, b=2)
test_1(a=1, b=5, c=7)