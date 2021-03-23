import os

with open("resources/file_remove_extra_spaces.txt", 'r') as word_file:
    with open("resources/temp.txt", "w") as temp_file:
        for line in word_file.readlines():
            temp_file.write(" ".join(line.split()) + "\n")

os.rename("resources/temp.txt", "resources/file_remove_extra_spaces.txt")
