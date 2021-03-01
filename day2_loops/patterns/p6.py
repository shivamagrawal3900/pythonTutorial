"""
    *
   **
  ***
 ****
*****
"""
a1 = int(input("Enter a number: "))

for i in range(a1):
    print(" " * (a1 - i - 1), end="")
    print("*" * (i + 1))
