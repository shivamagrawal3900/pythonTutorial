def get_fibonacci_n(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return get_fibonacci_n(n - 1) + get_fibonacci_n(n - 2)


# 0 1 1 2 3 5 8
n1 = int(input("Enter a number: "))
print("element number", n1, "in fibonacci series:", get_fibonacci_n(n1))
