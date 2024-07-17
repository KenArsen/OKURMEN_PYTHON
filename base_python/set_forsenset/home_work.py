# 1 - Тапшырма
'''
Консольго - боштук менен ажыратылган создор киргизилет.
Ал жазылган создордун ичинен уникалдуу создордун санын чыгарыныз.

Мисалы:
Мама мыла раму а потом мыла кота и еще мыла пол
Жоопко: 9
'''
words = map(str, input().split())
print(len(set(words)))


# 2 - Тапшырма
'''
Консольго - бир текст берилет.
Ошол текстин ичинде кандай цифралар бар экенин чыгарыныз
(регистр каралбайт)

Мисалы:
1)  Python 3.9.11 - best language!
    Жоопко: 1 3 9
2)
    C++ v. 0.22.12
    Жоопко: 0 1 2
'''
text = input()
digits_set = set()
for letter in text:
    if letter.isdigit():
        digits_set.add(letter)
for digit in digits_set:
    print(digit, end=' ')
print()

