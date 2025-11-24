# PE05 Q1 - Concatenate dictionaries
# Sample dicts
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# 새 딕셔너리를 만들고 세 딕셔너리를 차례대로 합친다
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

print("Result:", result)
# Expected: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
