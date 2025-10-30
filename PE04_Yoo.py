# PE04 – Lists and Tuples
# Name: Young Yoo
# Course: CS11A

# 1) Dinner Guests

# Initial guest list
guests = ["David", "Grace", "Niko"]
print("Initial guest list:", guests)

# One guest can't make it
print(f"\n{guests[1]} can't make it to dinner.")
guests[1] = "Evelyn"  # Replace guest
print("Updated guest list:", guests)

# Add new guests
guests.insert(0, "Michael")       # Add to beginning
guests.insert(2, "Sophia")        # Add to middle
guests.append("Daniel")           # Add to end
print("\nExpanded guest list:", guests)

# Remove guests until only two remain
print("\nSorry, I can only invite two people to dinner.")
while len(guests) > 2:
    removed = guests.pop()
    print(f"Sorry {removed}, I can't invite you to dinner.")

print("\nFinal guest list:", guests)

# 2) Animals and List Slicing

animals = ["dog", "cat", "tiger", "lion", "rabbit", "elephant", "monkey"]

print("\nAll animals:")
for animal in animals:
    print(animal)

print("\nThe first three items in the list are:", animals[:3])
print("Three items from the middle of the list are:", animals[2:5])
print("The last three items in the list are:", animals[-3:])

# 3) Duplicates in a List

numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
output_list = []

for num in numbers:
    if numbers.count(num) > 1 and num not in output_list:
        output_list.append(num)

print("\nList of duplicate elements:", output_list)

# 4) Buffet Menu (Tuples)

buffet_menu = ("pizza", "pasta", "salad", "soup", "ice cream")

print("\nOriginal buffet menu:")
for food in buffet_menu:
    print(food)

# Uncommenting next line would raise an error (tuples are immutable)
# buffet_menu[0] = "steak"

# Revised menu
buffet_menu = ("pizza", "sushi", "salad", "ramen", "cake")

print("\nRevised buffet menu:")
for food in buffet_menu:
    print(food)

# 5) Sort Tuples by Second Element

data = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
sorted_data = sorted(data, key=lambda x: x[1])

print("\nTuples sorted by the second item:", sorted_data)
