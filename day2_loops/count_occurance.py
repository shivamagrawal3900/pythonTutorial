a1 = int(input("Enter a number: "))
a2 = int(input("Enter a pivot: "))

output = 0
while a1 > 0:
    if a2 == (a1%10): output += 1
    a1 //= 10

if output > 0:
    print("Pivot occurred", output, "times")
else:
    print("Pivot not present in the number")