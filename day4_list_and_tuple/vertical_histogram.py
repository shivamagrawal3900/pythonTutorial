l1 = []
for i in range(10):
    l1.append(int(input(f"Enter {i+1} value: ")))

max_value = max(l1)

for i in range(max_value, 0, -1):
    for value in l1:
        if value >= i:
            print("*\t", end="")
        else:
            print("\t", end="")
    print()