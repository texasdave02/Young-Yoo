motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print("Original list:", motorcycles)

# Delete using del
del motorcycles[1]     # remove 'yamaha'
print("After del:", motorcycles)

# Pop last element
popped_motorcycle = motorcycles.pop()
print("After pop:", motorcycles)
print("Popped motorcycle:", popped_motorcycle)

# Remove using value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print("After remove:", motorcycles)