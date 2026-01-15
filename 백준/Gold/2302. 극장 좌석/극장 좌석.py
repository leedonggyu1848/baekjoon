import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = []
dp = [0] * 41
dp[0] = 1
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

for _ in range(int(input())):
    nums.append(int(input()))
nums.append(n+1)

bf = 0
rst = 1
for cur in nums:
    rst *= dp[cur-bf-1]
    bf = cur
print(rst)
