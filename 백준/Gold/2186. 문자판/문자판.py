import sys
input = sys.stdin.readline

ny, nx, k = map(int, input().split())
m = []
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

for _ in range(ny):
    m.append(input().rstrip())
tar = input().rstrip()
dp = [[[0] * (len(tar)+1) for _ in range(nx)] for _ in range(ny)]

for y in range(ny):
    for x in range(nx):
        if tar[len(tar)-1] == m[y][x]:
            dp[y][x][len(tar)-1] += 1

def is_range(y, x):
    return 0 <= y < ny and 0 <= x < nx

def cal(y, x, cur):
    for step in range(1, k+1):
        for i in range(4):
            cy = y + step * dy[i]
            cx = x + step * dx[i]
            if is_range(cy, cx):
                dp[y][x][cur] += dp[cy][cx][cur+1]


for i in reversed(range(len(tar)-1)):
    for y in range(ny):
        for x in range(nx):
            if tar[i] == m[y][x]:
                cal(y, x, i)

rst = 0
for y in range(ny):
    for x in range(nx):
        rst += dp[y][x][0]
print(rst)

