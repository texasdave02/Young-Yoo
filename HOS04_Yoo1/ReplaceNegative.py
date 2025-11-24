numbers = [10, -20, 30, -40, 50]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = abs(numbers[i])

print("Updated list:", numbers)
