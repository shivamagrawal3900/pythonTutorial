a1 = input("Enter a string: ")

my_list = a1.split()
output = ""
for word in my_list:
    output = output + " " +word
output = output.strip()
print("Without extra spaces:", output)