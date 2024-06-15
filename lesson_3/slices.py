text = "I know you are trying really hard to learn1Python." # Python learn

word = text[2:6]
print(word)

# [:10] 0 индекстен 10чу индекске чейин
word = text[:17]
print(word)

# [10:] 10 индекстен аягына чейин
word = text[20:]
print(word)

word = text [37:42]
d = text [43:49]
print( d , word)

text = "I konw you are trying really hard to learn1Python."

# [1:2:10] start:end:step = башы:аягы:кадамы
word = text[1:20:10] 
print(word)

# [-1] аягынан биринчи символду алат
word = text[-5:-2]
print(word)


text = "I konw you are trying really hard to learn1Python."
words = text[2:-2:2] # [2:-2:1]
print(words)

text = "Kyrgyzstan"
print(text[1:4:1])