marks = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

def get_key(item):
    return item[0]

sorted_marks = sorted(marks, key=get_key)
print(sorted_marks)
