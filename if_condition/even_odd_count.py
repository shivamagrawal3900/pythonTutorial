a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))

even_count = odd_count = 0

if a1 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
if a2 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
if a3 % 2 == 0:
    even_count += 1
else:
    odd_count += 1
if a4 % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print("Number of even values: ", even_count)
print("Number of odd values: ", odd_count)
