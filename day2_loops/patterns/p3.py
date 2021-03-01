"""
    1
   121
  12321
 1234321
123454321
"""
a1 = int(input("Enter a number: "))

for i in range(a1):
    print(" "*(a1-i-1), end="")
    for i2 in range(i+1):
        print(str(i2 + 1), end="")
    for i2 in range(i, 0, -1):
        print(str(i2), end="")
    print()
