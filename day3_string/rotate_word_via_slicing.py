a1 = input("Enter a word:\n")

for i in range(1, len(a1) + 1):
    print(a1[i:], a1[:i], sep="")
