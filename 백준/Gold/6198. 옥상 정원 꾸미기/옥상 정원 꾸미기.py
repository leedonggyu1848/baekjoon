import sys
input = sys.stdin.readline

n = int(input())
buildings = [int(input()) for _ in range(n)]
s = []
rst = 0

for i, height in enumerate(buildings):
    while s and s[-1][1] <= height:
        rst += i - s.pop()[0] - 1
    s.append((i, height))

while s:
    rst += n - s.pop()[0] - 1
print(rst)

