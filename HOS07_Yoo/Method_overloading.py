class MathOperations:
    def sum(self, a, b, c=0):
        return a + b + c


m = MathOperations()

print(m.sum(3, 4))       # c는 기본값 0
print(m.sum(3, 4, 5))    # c에 5 사용
