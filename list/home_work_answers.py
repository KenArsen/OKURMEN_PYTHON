# 1 - Тапшырма
'''
Консольдон биз создоруду жазабыз жана ал создорду 
ар бир сапка чыгарыныздар
'''
# words = input("Enter your words: ")
# words_list = words.split()
# for word in words_list:
#     print(word)
# print(*words.split(), sep='\n')

# 2 - Тапшырма
'''
Бизге ФИО киргизебиз, жоопко баш тамгаларды чыгарыныз
Мисалы:
Кенжегулов Арсен Кенжегулович
жооп:
К.А.К деп чыгыш керек
'''

# F_I_O = input("Enter you FIO: ")
# f_i_o = F_I_O.split()
# print(f_i_o)
# print(f'{f_i_o[0][0]}.{f_i_o[1][0]}.{f_i_o[2][0]}')

# 3 - Тапшырма
'''
Биз консольдон 4 сан ортосу чекит 
менен ажыратылган текст(ip address) киргизебиз
(192.168.255.223)

Биз текшеришибиз керек ошол ip адрес туура жазылганын
Эскертүү. Эгерде бардык 4 сан 0 дон 255 ке чейин болсо, IP адрес туура болот.
Мисалы:
192.168.0.3 деп киргизсек
жоопко:
Yes

192.168.0.300 деп киргизсек
жоопко:
No
'''

# ip_address = input("Enter your ip address: ")
# i_a = ip_address.split('.')
# print(i_a)
# for ip in i_a:
#     if int(ip) < 0 or int(ip) > 255:
#         print("No")
#         break
# else:
#     print("Yes")


# 4 - Тапшырма
'''
numbers = [8, 9, 10, 11]
Берилген кодду төмөнкүдөй кылып толтуруңуз:

    тизменин экинчи элементин 17 менен алмаштырыныз;
    Тизменин аягына 4, 5 жана 6 сандарын кошунуз;
    Тизменин биринчи элементин алып салыныз;
    3 индекске 25 санын кошунуз;
    print() функциясын колдонуп тизмени басып чыгарыныз
'''
# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# print(numbers)
# numbers.extend([4,5,6])
# print(numbers)
# numbers.pop(0)
# print(numbers)
# numbers.insert(3, 25)
# print(numbers)