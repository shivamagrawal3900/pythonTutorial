"""
1
222
33333
4444444
555555555
"""
a1 = int(input("Enter a number: "))

for i in range(a1):
    print(str(i + 1) * ((i + 1) + i ))