import sys
from collections import deque
input = sys.stdin.readline

dys = [0, 1, 0, -1]
dxs = [-1, 0, 1, 0]
ys, xs = map(int, input().split())
# 0: space, 1: fire 2: wall
board = [[0] * xs for _ in range(ys)]
visited = [[False] * xs for _ in range(ys)]

fire = deque()
q = deque()
for y in range(ys):
    s = input().rstrip()
    for x in range(xs):
        c = s[x]
        if c == '#':
            board[y][x] = 2
        elif c == '.':
            board[y][x] = 0
        elif c == 'J':
            board[y][x] = 0
            visited[y][x] = True
            q.append((y, x, 0))
        elif c == 'F':
            board[y][x] = 1
            fire.append((y, x, 0))

time = 0

def is_range(y, x):
    if 0 <= y < ys and 0 <= x < xs:
        return True
    return False

def spread_fire():
    global fire, board
    while fire:
        if fire[0][2] != time:
            break
        y, x, t = fire.popleft()
        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx
            if is_range(ny, nx) and board[ny][nx] == 0:
                board[ny][nx] = 1
                fire.append((ny, nx, t+1))

while q:
    y, x, t = q.popleft()
    if time != t:
        spread_fire()
        time += 1
    if board[y][x] != 0:
        continue
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if not is_range(ny, nx):
            print(time+1)
            exit(0)
        if  board[ny][nx] == 0 and not visited[ny][nx]:
            q.append((ny, nx, time+1))
            visited[ny][nx] = True

print('IMPOSSIBLE')
