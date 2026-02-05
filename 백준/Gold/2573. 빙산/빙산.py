import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

sy, sx = map(int, input().split())
board = []
for _ in range(sy):
    board.append(list(map(int, input().split())))

q = deque()
for y in range(sy):
    for x in range(sx):
        if board[y][x] != 0:
            q.append((y, x))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
def count(y, x):
    visited = [[False] * sx for _ in range(sy)]
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    rst = 1
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < sy and 0 <= nx < sx:
                if board[ny][nx] != 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True
                    rst += 1
    return rst

day = 0
while True:
    if not q:
        print(0)
        break
    if count(q[0][0], q[0][1]) != len(q):
        print(day)
        break
    day += 1
    buf = deque()
    while q:
        cy, cx = q.pop()
        cv = 0
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < sy and 0 <= nx < sx:
                if board[ny][nx] == 0:
                    cv += 1
        buf.append((cy, cx, board[cy][cx] - cv))
    while buf:
        cy, cx, cv = buf.pop()
        board[cy][cx] = max(cv, 0)
        if board[cy][cx] > 0:
            q.append((cy, cx))
        

