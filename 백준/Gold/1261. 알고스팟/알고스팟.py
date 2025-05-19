import sys
from collections import deque
input = sys.stdin.readline


xs, ys = map(int, input().split())
dys = [1, -1, 0, 0]
dxs = [0, 0, 1, -1]
is_wall = [[False] * xs for _ in range(ys)]
is_visited = [[False] * xs for _ in range(ys)]

for y in range(ys):
    s = input()
    for x in range(xs):
        is_wall[y][x] = False if s[x] == '0' else True

def is_range(y, x):
    if 0 <= x < xs and 0 <= y < ys:
        return True
    return False

q = deque()
q.append((0, 0, 0))
is_visited[0][0] = True
rst = 0
while q:
    y, x, rst = q.pop()
    if y == ys-1 and x == xs-1:
        break
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if is_range(ny, nx) and not is_visited[ny][nx]:
            if is_wall[ny][nx]:
                q.appendleft((ny, nx, rst+1))
            else:
                q.append((ny, nx, rst))
            is_visited[ny][nx] = True

print(rst)
