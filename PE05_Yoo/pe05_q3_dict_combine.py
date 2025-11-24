# PE05 Q3 - Combine two dictionaries adding values for common keys

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

# 결과를 저장할 새 딕셔너리
result = {}

# d1과 d2의 모든 키 집합을 구한다
all_keys = set(d1.keys()) | set(d2.keys())

# 각 키에 대해 d1과 d2의 값을 더해준다 (없는 키는 0으로 처리)
for key in all_keys:
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print("Combined dictionary:", result)
# One possible print order: {'a': 400, 'b': 400, 'c': 300, 'd': 400}
