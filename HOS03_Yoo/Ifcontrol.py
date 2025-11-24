number = int(input("Enter an integer: "))

if number < 0:
    print("Number is negative")
elif number == 0:
    print("Number is zero")
else:
    if number % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
