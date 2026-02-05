import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
dp = [[0] * 2 for _ in range(n)]
dp[0][0] = nums[0]
if n != 1:
    dp[1][0] = nums[1]
    dp[1][1] = nums[0] + nums[1]

for i in range(2, n):
    dp[i][0] = max(dp[i-2]) + nums[i]
    dp[i][1] = dp[i-1][0] + nums[i]

print(max(dp[n-1]))
