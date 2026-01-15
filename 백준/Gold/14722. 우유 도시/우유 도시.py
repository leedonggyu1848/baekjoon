import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = []

dy = [0, -1]
dx = [-1, 0]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    m.append(list(map(int, input().split())))

def get(y, x, i):
    if 0 <= y < n and 0 <= x < n:
        return dp[y][x][i]
    return 0


for y in range(n):
    for x in range(n):
        for i in range(3):
            dp[y][x][i] = max(get(y-1, x, i), get(y, x-1, i))
        if dp[y][x][(m[y][x]-1+3) % 3] != 0:
            dp[y][x][m[y][x]] = max(dp[y][x][(m[y][x]-1+3) % 3]+1, dp[y][x][m[y][x]])
        elif m[y][x] == 0:
            dp[y][x][0] = max(dp[y][x][0], 1)

print(max(dp[n-1][n-1]))
