a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))

a3 = a1 if a1 < a2 else a2
a3 += 1

output = 1
for i in range(2, a3):
    if (a1 % i == 0) and (a2 % i == 0): output = i

print("Greatest common divisor:", output)