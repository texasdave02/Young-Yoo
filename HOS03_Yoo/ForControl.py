import random

start = 1
end = random.randint(5, 15)

print("Start:", start)
print("End:", end)
print("Numbers in range:")

for i in range(start, end):
    print(i)
