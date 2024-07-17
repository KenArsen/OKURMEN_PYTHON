# words = input("Сөздөрдү киргизиңиз (боштук менен бөлүп): ").split()

# word_lengths = {word: len(word) for word in words}

# print(word_lengths)


print("Сөздөрдү киргизиңиз (боштук менен бөлүп):", end=" ")

words = [word for word in input().split()]

word_lengths = dict()

for word in words:
    word_lengths[word] = len(word)

print(word_lengths)