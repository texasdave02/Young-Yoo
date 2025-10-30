# Binary Search Implementation
# CS11A - PE02_Yoo.ipynb
# Student: Young Yoo

def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return None

# Test data
my_list = [1, 3, 5, 7, 9, 11, 13]
print("List:", my_list)

# Test search
print("Find 7 → Index:", binary_search(my_list, 7))
print("Find 9 → Index:", binary_search(my_list, 9))
print("Find 2 → Index:", binary_search(my_list, 2))

# Add more values to test correctness
my_list.extend([15, 17, 19])
my_list.sort()
print("\nUpdated List:", my_list)
print("Find 17 → Index:", binary_search(my_list, 17))
