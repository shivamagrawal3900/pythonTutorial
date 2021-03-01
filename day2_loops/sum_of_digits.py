a1 = int(input("Enter a number: "))
output = 0
while a1 > 0:
    output += (a1 % 10)
    a1 //= 10

print("Sum of digits:", output)