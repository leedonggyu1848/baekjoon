import sys

n = int(sys.stdin.readline())
weights = []
for _ in range(n):
    weights.append(int(sys.stdin.readline()))

weights.sort(reverse=True)

rst = 0
for i in range(n):
    rst = max(rst, weights[i] * (i+1))
print(rst)
