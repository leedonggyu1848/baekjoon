import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(n+1)]
maxv = 0
for num in map(int, input().split()):
    dp[num] = dp[num-1] + 1
    maxv = max(maxv, dp[num])
print(n-maxv)
