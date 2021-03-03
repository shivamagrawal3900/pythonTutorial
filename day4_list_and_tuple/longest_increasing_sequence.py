l1 = []
for i in range(10):
    l1.append(int(input(f"Enter {i+1} value: ")))

max_sequence = current_sequence = 1
for i in range(len(l1) - 1):
    if l1[i] <= l1[i+1]:
        current_sequence += 1
    else:
        if current_sequence > max_sequence:
            max_sequence = current_sequence
        current_sequence = 1
else:
    if current_sequence > max_sequence:
        max_sequence = current_sequence
print("Max sequence is: ", max_sequence)