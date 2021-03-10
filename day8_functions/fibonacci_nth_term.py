def get_fibonacci_n(n):
    return fibonacci_n_helper(n)


def fibonacci_n_helper(n, i=1, a=0, b=1):
    return a if n <= i else fibonacci_n_helper(n, i + 1, b, a + b)

    # if n <= i:
    #     print(a)
    #     return a
    # print(a, end=" ")
    # return fibonacci_n_helper(n, i + 1, b, a + b)


n1 = int(input("Enter a number: "))
print("element number", n1, "in fibonacci series:", get_fibonacci_n(n1))
