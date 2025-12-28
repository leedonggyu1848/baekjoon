import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(map(int, input().split()))

def check(a, b):
    if a < 0 or b < 0:
        return False
    return dp[a][b]

dp = [[False] * (sum(nums)+1) for _ in range(sum(nums)+1)]
dp[0][0] = True
total = 0
for i in range(n):
    total += nums[i]
    for a in range(total, -1, -1):
        for b in range(total-a, -1, -1):
            dp[a][b] |= check(a-nums[i], b) | check(a, b-nums[i])

rst = 0
for a in range(total):
    for b in range(total-a):
        if dp[a][b]:
            c = total - a - b
            rst = max(rst, min(a, b, c))
print(rst)
