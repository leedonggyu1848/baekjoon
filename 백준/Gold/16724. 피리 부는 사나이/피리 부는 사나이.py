import sys
input = sys.stdin.readline

sy, sx = map(int, input().split())

visited = [[-1] * sx for _ in range(sy)]
board = [[None] * sx for _ in range(sy)]

for y in range(sy):
    s = input().rstrip()
    for x in range(sx):
        if s[x] == 'U':
            board[y][x] = 0
        elif s[x] == 'D':
            board[y][x] = 1
        elif s[x] == 'L':
            board[y][x] = 2
        elif s[x] == 'R':
            board[y][x] = 3

rst = 0
dy = [-1, 1, 0, 0] # u d l r
dx = [0, 0, -1, 1]
def is_range(y, x):
    global sy, sx
    return 0 <= y < sy and 0 <= x < sx

def dfs(y, x, time):
    d = board[y][x]
    ny = y + dy[d]
    nx = x + dx[d]
    if is_range(ny, nx):
        if visited[ny][nx] < 0:
            visited[ny][nx] = time
            return dfs(ny, nx, time)
        else:
            return visited[ny][nx]  == time
time = 0
for y in range(sy):
    for x in range(sx):
        if visited[y][x] == -1:
            visited[y][x] = time
            rst += dfs(y, x, time)
            time += 1
print(rst)
