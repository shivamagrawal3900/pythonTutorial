min = max = None
for i in range(10):
    a = int(input("Enter " + str(i + 1) + " number: "))
    if not max or a > max: max = a
    if not min or a < min: min = a

print("Max number:", max)
print("Min number:", min)
