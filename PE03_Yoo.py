# PE03_Yoo.py
# CS11A
# Student: Young Yoo

# 1. check prime number
num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


# 2. fibonacci numbers
def fib(n):
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

count = int(input("\nHow many fibonacci numbers? "))
print("Fibonacci numbers:", fib(count))


# 3. stage of life
age = int(input("\nEnter your age: "))

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are an elder")


# 4. movie ticket price
print("\nEnter 'quit' to stop")
while True:
    age_in = input("Enter age: ")
    if age_in.lower() == 'quit':
        break
    age = int(age_in)

    if age < 3:
        print("Ticket is free")
    elif age <= 12:
        print("Ticket is $10")
    else:
        print("Ticket is $15")


# 5. pattern printing
rows = 4
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
