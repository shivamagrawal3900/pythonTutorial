s1 = input("Enter a string: ")
words = s1.split()

word_frequency = {}
unique_words = set()

for word in words:
    # word = word.lower()
    if word in unique_words:
        word_frequency[word] += 1
    else:
        unique_words.add(word)
        word_frequency[word] = 1

print(word_frequency)