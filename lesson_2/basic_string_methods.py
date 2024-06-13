text = 'Sabak213' # str

'''
text озормосу жалан тамгалардан турса 
.isalpha() функциясы бизге True(Чын) деген маани кайтарат,
егер андай болбосо False(Жалган) деген маани кайтарат
'''
print(text.isalpha()) 

text = 'okurmen'
print(text.islower())

text = 'OKURMENa'
print(text.isupper())

text = "Erbol Kudakeev"
print(text.startswith("Erbol"))

text = "Erbol Kudakeev"
print(text.endswith(""))

text = "Erbol Kudakeev"
print(text.lower()) # erbol kudakeev

text = "Erbol Kudakeev"
print(text.upper()) # ERBOL KUDAKEEV

text = "erbol kudakeev asdjfl aldjf a;lkfdj"
print(text.title())

text = "erbol kudakeev jfo aljdfo alkd"
print(text.capitalize())


text = "Hello, I study in Okurmen"    
print(text.find("h"))

text = "Hello, I study in Okurmen"    
print(text.replace("Okurmen", 'booster'))

text = "Hello, I study, in Okurmen"    
print(text.split("study"))

people = 'Arsen, Amantur, Hadizha, Ibragim'
persons = people.split(',')



