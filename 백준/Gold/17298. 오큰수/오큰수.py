import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
rst = [-1] * n
s = []

for i, a in enumerate(arr):
    while s and s[-1][1] < a:
        rst[s.pop()[0]] = a
    s.append((i, a))

print(*rst)
