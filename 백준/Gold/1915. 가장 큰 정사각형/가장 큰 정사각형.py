import sys
import math
input = sys.stdin.readline

sy, sx = map(int, input().split())
dp = [[0] * sx for _ in range(sy)]
dy = [-1, -1, 0]
dx = [-1, 0, -1]

def is_range(y, x):
    return 0 <= y < sy and 0 <= x < sx

for y in range(sy):
    s = input().rstrip()
    for x in range(sx):
        if s[x] == '0':
            continue
        minv = math.inf
        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if not is_range(ny, nx):
                minv = 0
                break
            minv = min(minv, dp[ny][nx])
        dp[y][x] = minv + 1

print(max(map(max, dp)) ** 2)
