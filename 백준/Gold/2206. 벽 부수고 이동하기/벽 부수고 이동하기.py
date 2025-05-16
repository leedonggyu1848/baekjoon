import sys
from collections import deque
input = sys.stdin.readline

dxs = (0,1,0,-1)
dys = (-1,0,1,0)
sy, sx = map(int, input().split())
board = [[0] * sx for _ in range(sy)]
# y, x, 벽을 부셨는지
# 0이 안부심, 1이 부심
visited = [[[-1] * 2 for _ in range(sx)] for _ in range(sy)]
for y in range(sy):
    s = input().rstrip()
    for x in range(sx):
        board[y][x] = int(s[x])

q = deque()
q.append((0, 0, 0)) # y, x, 부셧나
visited[0][0][0] = 1

def is_range(y, x):
    global sy, sx
    if 0 <= y < sy and 0 <= x < sx:
        return True
    return False

while q:
    y, x, b = q.popleft()
    if y == sy-1 and x == sx-1:
        break;
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if is_range(ny, nx):
            if b == 0 and board[ny][nx] == 1 and visited[ny][nx][1] == -1:
                visited[ny][nx][1] = visited[y][x][b] + 1
                q.append((ny, nx, 1))
            if visited[ny][nx][b] == -1 and board[ny][nx] == 0:
                visited[ny][nx][b] = visited[y][x][b] + 1
                q.append((ny, nx, b))

rst = visited[sy-1][sx-1]
if not -1 in rst:
    print(min(rst))
else:
    print(max(rst))
