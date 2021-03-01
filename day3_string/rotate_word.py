a1 = input("Enter a word: ")

l = len(a1)
for i in range(l + 1):
    i2 = i
    for i3 in range(l):
        print(a1[(i2 + i3) % l], end="")
    print()
