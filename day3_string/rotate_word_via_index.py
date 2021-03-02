a1 = input("Enter a word:\n")

l = len(a1)
for i in range(l):
    for i2 in range(l):
        print(a1[(i + i2 + 1) % l], end="")
    print()
