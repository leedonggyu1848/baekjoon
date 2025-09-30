import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

sy, sx = map(int, input().split())
board = []

for y in range(sy):
    board.append(list(map(int, input().split())))


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

dp = [[-1] * sx for _ in range(sy)]
dp[sy-1][sx-1] = 1

def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < sy and 0 <= nx < sx and board[ny][nx] < board[y][x]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]

print(dfs(0, 0))