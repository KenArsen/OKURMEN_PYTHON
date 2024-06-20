# 1 - Тапшырма
'''
Биз консольдон бир сан киргизебиз(n деген сан болсун).
Жоопко [1,2,3,..., n] чыгарыш керек
''' 
n = int(input("Enter a number: "))
numbers = list()
for i in range(1, n+1):
    numbers.append(i)
print(numbers)


# 2 - Тапшырма
'''
Биз консольдон бир сан киргизебиз(n деген сан болсун).
Англис тамгаларын катары менен n тамгасын чыгарыныз
'''
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input("Enter a number: "))
print(letters[:n])


# 3 - Тапшырма
'''
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
ушул элементтердин орточо суммасын табыныздар(среднее арифметическое)
'''
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
sum_evens = 0
for even in evens:
    sum_evens += even
length = len(evens)
avarage = sum_evens / length
print(avarage)


# 4 - Тапшырма
'''
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
ушул листтин ичинен Green барабар болгон созду Жашыл деген созго жана
Red деген созду Кызыл деген созго алмаштырып жоопту консольго чыгарыныздар
'''
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[0] = 'Кызыл'
rainbow[3] = 'Жашыл'
print(rainbow)


