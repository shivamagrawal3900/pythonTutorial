with open("resources/file_word_frequenct.txt") as word_file:
    word_frequency = {}
    for line in word_file.readlines():
        for word in line.split():
            word_frequency[word] = word_frequency.get(word, 0) + 1
print(word_frequency)
