import sys
import math
input = sys.stdin.readline

t, move = map(int, input().split())
dp = [[[-math.inf] * (2) for _ in range(move+1)] for _ in range(t)]
down = []
for _ in range(t):
    down.append(int(input())-1)

if down[0] == 0:
    dp[0][0][0] = 1
else:
    dp[0][0][0] = 0
    dp[0][1][1] = 1

for cur in range(t-1):
    for i in range(move+1):
        if dp[cur][i][0] != -math.inf:
            if i < move:
                dp[cur+1][i+1][1] = max(dp[cur][i][0]+(down[cur+1] == 1), dp[cur+1][i+1][1])
            dp[cur+1][i][0] = max(dp[cur][i][0]+(down[cur+1] == 0), dp[cur+1][i][0])
        if dp[cur][i][1] != -math.inf:
            if i < move:
                dp[cur+1][i+1][0] = max(dp[cur][i][1]+(down[cur+1]==0), dp[cur+1][i+1][0])
            dp[cur+1][i][1] = max(dp[cur][i][1]+(down[cur+1]==1), dp[cur+1][i][1])

rst = 0
for i in range(move+1):
    rst = max(rst, *dp[t-1][i])

print(rst)

