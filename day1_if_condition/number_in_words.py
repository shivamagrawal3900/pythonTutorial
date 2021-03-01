a1 = int(input("Enter 4 digit number: "))

if a1 >= 1000:
    digit = a1 // 1000
    if digit == 1:
        print("One", end=" ")
    elif digit == 2:
        print("Two", end=" ")
    elif digit == 3:
        print("Three", end=" ")
    elif digit == 4:
        print("Four", end=" ")
    elif digit == 5:
        print("Five", end=" ")
    elif digit == 6:
        print("Six", end=" ")
    elif digit == 7:
        print("Seven", end=" ")
    elif digit == 8:
        print("Eight", end=" ")
    elif digit == 9:
        print("Nine", end=" ")
    print("Thousand", end=" ")
if a1 >= 100:
    digit = (a1 % 1000) // 100
    if digit > 0:
        if digit == 1:
            print("One", end=" ")
        elif digit == 2:
            print("Two", end=" ")
        elif digit == 3:
            print("Three", end=" ")
        elif digit == 4:
            print("Four", end=" ")
        elif digit == 5:
            print("Five", end=" ")
        elif digit == 6:
            print("Six", end=" ")
        elif digit == 7:
            print("Seven", end=" ")
        elif digit == 8:
            print("Eight", end=" ")
        elif digit == 9:
            print("Nine", end=" ")
        print("Hundred", end=" ")

digit = (a1 % 100)
if digit > 0:
    if 10 <= digit <= 19:
        if digit == 10:
            print("Ten", end=" ")
        elif digit == 11:
            print("Eleven", end=" ")
        elif digit == 12:
            print("Twelve", end=" ")
        elif digit == 13:
            print("Thirteen", end=" ")
        elif digit == 14:
            print("Fourteen", end=" ")
        elif digit == 15:
            print("Fiveteen", end=" ")
        elif digit == 16:
            print("Sixteen", end=" ")
        elif digit == 17:
            print("Seventeen", end=" ")
        elif digit == 18:
            print("Eighteen", end=" ")
        elif digit == 19:
            print("Nineteen", end=" ")
    else:
        if digit >= 20:
            digit1 = digit // 10
            if digit1 == 2:
                print("Twenty", end=" ")
            elif digit1 == 3:
                print("Thirty", end=" ")
            elif digit1 == 4:
                print("Forty", end=" ")
            elif digit1 == 5:
                print("Fifty", end=" ")
            elif digit1 == 6:
                print("Sixty", end=" ")
            elif digit1 == 7:
                print("Seventy", end=" ")
            elif digit1 == 8:
                print("Eighty", end=" ")
            elif digit1 == 9:
                print("Ninety", end=" ")
        digit2 = digit % 10
        if digit2 == 1:
            print("One", end=" ")
        elif digit2 == 2:
            print("Two", end=" ")
        elif digit2 == 3:
            print("Three", end=" ")
        elif digit2 == 4:
            print("Four", end=" ")
        elif digit2 == 5:
            print("Five", end=" ")
        elif digit2 == 6:
            print("Six", end=" ")
        elif digit2 == 7:
            print("Seven", end=" ")
        elif digit2 == 8:
            print("Eight", end=" ")
        elif digit2 == 9:
            print("Nine", end=" ")
elif a1 == 0:
    print("Zero")
