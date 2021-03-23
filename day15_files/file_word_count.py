with open("resources/file_word_count.txt") as word_file:
    word_count = 0
    for line in word_file.readlines():
        word_count += len(line.split())
    print(word_count)