# .format()
# % 
# f''
message = "I love Kyrgyzstan" 
kyrgyzstan = message[-10:]
love = message[2:-11]
print(kyrgyzstan, love)
print("I very {0} my {1} - {2}".format(love, kyrgyzstan, "123"))
print(f"I very {love} my {love} {kyrgyzstan}")

float_number = 23.455840928
f_text = f'float number = {float_number:.2f}'
print(f_text)
https://www.w3schools.com/python/ref_string_format.asp

