import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
left = [0] * n
right = [0] * n
idx = [[] for _ in range(n)]

def fill(enum, cache):
    s = []
    for i, n in enum:
        while s and s[-1][0] <= n:
            s.pop()
        if s:
            idx[i].append(s[-1][1])
        cache[i] = len(s)
        s.append((n, i))

fill(enumerate(nums), left)
fill(reversed(list(enumerate(nums))), right)
for i in range(n):
    rst = left[i] + right[i]
    if rst == 0:
        print(rst)
    else:
        if len(idx[i]) == 1:
            print(rst, idx[i][0] + 1)
        else:
            print(rst, idx[i][0] + 1 if abs(idx[i][0] - i) <= abs(idx[i][1] - i) else idx[i][1] + 1)

