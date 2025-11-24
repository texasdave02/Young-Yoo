# PE05 Q2 - Create a dictionary of x: x*x for numbers 1..n

# n 값을 입력받는다
n = int(input("Enter a positive integer n: "))

# 1부터 n까지의 제곱 값을 딕셔너리로 생성
result = {}
for x in range(1, n + 1):
    result[x] = x * x

print("Result:", result)
# Sample for n = 5: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
