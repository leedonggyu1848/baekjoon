import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append([int(c) for c in input().rstrip()])

dp = [[[-1] * (1 << n) for _ in range(10)] for _ in range(n)]

def dfs(mask, cost, cur):
    if dp[cur][cost][mask] != -1:
        return dp[cur][cost][mask]
    dp[cur][cost][mask] = 0
    for nxt in range(n):
        nxt_bit = 1 << nxt
        if nums[cur][nxt] >= cost and (mask & nxt_bit) == 0:
            dp[cur][cost][mask] = max(dp[cur][cost][mask], 1 + dfs(mask|nxt_bit, nums[cur][nxt], nxt))
    return dp[cur][cost][mask]

dp[0][0][0] =  1 + dfs(1, 0, 0)
print(dp[0][0][0])
