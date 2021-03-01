a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))

min_value = max_value = a1

if max_value < a2:
    max_value = a2
elif min_value > a2:
    min_value = a2

if max_value < a3:
    max_value = a3
elif min_value > a3:
    min_value = a3

if max_value < a4:
    max_value = a4
elif min_value > a4:
    min_value = a4

print("minimum value: ", min_value)
print("maximum value: ", max_value)
