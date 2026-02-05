import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,a,b = map(int, input().split())
    board[y-1][x-1].append((b-1, a-1))

visited = [[False] * n for _ in range(n)]
light = [[False] * n for _ in range(n)]
light[0][0] = True
visited[0][0] = True

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def next_pos(y, x):
    rst = []
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            rst.append((ny, nx))
    return rst

def turn_on(q, y, x):
    rst = 0
    for ly, lx in board[y][x]:
        if light[ly][lx]: continue
        rst += 1
        light[ly][lx] = True
        for ny, nx in next_pos(ly, lx):
            if light[ny][nx] and visited[ny][nx]:
                visited[ly][lx] = True
                q.append((ly, lx))
                break
    return rst

q = deque()
q.append((0,0))
rst = 1
while q:
    y, x = q.popleft()
    rst += turn_on(q, y, x)
    for ny, nx in next_pos(y, x):
        if light[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = True
            q.append((ny, nx))

print(rst)
