num = int(input("Enter a number less than 100: "))

while num >= 100:
    print("Number is greater than or equal to 100. Try again.")
    num = int(input("Enter a number less than 100: "))

print("Thank you. Your number is", num)
