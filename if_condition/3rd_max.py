a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))

max1 = a1

if max1 <= a2:
    max2 = max1
    max1 = a2
else:
    max2 = a2

if max1 <= a3:
    max3 = max2
    max2 = max1
    max1 = a3
elif max2 <= a3:
    max3 = max2
    max2 = a3
else:
    max3 = a3

if max3 <= a4:
    if max2 <= a4:
        if max1 <= a4:
            max3 = max2
            max2 = max1
            max1 = a4
        else:
            max3 = max2
            max2 = a4
    else:
        max3 = a4

print("3rd max value is: ", max3)