import sys
input = sys.stdin.readline

n = int(input())
dp = [False] * 1001
# 1, 3, 4
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True


for i in range(5, n+1):
    dp[i] = not (dp[i-1] and dp[i-3] and dp[i-4])

print("SK" if dp[n] else "CY")
