"""
0
12
345
6789
01234
"""
a1 = int(input("Enter a number: "))
a2 = 0

for i in range(a1):
    for i2 in range(i+1):
        print(a2, end="")
        a2 = 0 if a2 == 9 else (a2 + 1)
    print()
