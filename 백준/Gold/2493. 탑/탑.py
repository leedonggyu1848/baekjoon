n = int(input())
towers = list(map(int, input().split()))
s = []
rst = [0] * n
for i, v in enumerate(towers[::-1]):
    while s and v > s[-1][1]:
        rst[s.pop()[0]] = n - i
    s.append((i, v))
print(*rst[::-1])
