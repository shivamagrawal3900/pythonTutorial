import os

with open("resources/file_words_to_upper.txt", 'r') as word_file:
    with open("resources/temp.txt", "w") as temp_file:
        for line in word_file.readlines():
            temp_file.write(line.upper() + "\n")

os.rename("resources/temp.txt", "resources/file_words_to_upper.txt")
