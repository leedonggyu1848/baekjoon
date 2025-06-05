import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

sy, sx = map(int, input().split())
board = [[None] * sx for _ in range(sy)]
dp = [[-1] * sx for _ in range(sy)]
for y in range(sy):
    c = input()
    for x in range(sx):
        board[y][x] = 0 if c[x] == 'H' else int(c[x])

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def is_range(y, x):
    return 0 <= y < sy and 0 <= x < sx

def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = math.inf
    v = 1
    weight = board[y][x]
    if weight == 0:
        dp[y][x] = 0
        return dp[y][x]
    for i in range(4):
        ny = y + dy[i] * weight
        nx = x + dx[i] * weight
        if is_range(ny, nx):
            v = max(dfs(ny, nx)+1, v)
    dp[y][x] = v
    return dp[y][x]

rst = dfs(0, 0)
if rst == math.inf:
    print('-1')
else:
    print(rst)
