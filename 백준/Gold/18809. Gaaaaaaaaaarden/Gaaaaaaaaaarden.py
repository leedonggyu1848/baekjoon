import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

class g:
    WATER = 0
    SOIL = 1
    FLOWER = -1
    RED = 0
    GREEN = 1

ys, xs, gs, rs = map(int, input().split())
plate = [[g.WATER] * xs for _ in range(ys)]
board = [[g.WATER] * xs for _ in range(ys)]
cnds = []
rst = 0

for y in range(ys):
    row = list(map(int, input().split()))
    for x in range(xs):
        if row[x] != g.WATER:
            plate[y][x] = g.SOIL
            if row[x] == 2:
                cnds.append((y, x))

def is_range(y, x):
    global ys, xs, board
    if 0 <= y < ys and 0 <= x < xs:
        return True
    return False

def spread(q, visited, time, color):
    global ys, xs, board
    cnt = len(q)
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    ret = 0
    for _ in range(cnt):
        y, x = q.popleft()
        if board[y][x] == g.FLOWER:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_range(ny, nx) and not visited[ny][nx][color]: # 방문한 적 없으면 추가
                visited[ny][nx][color] = True
                if board[ny][nx] == time:
                    board[ny][nx] = g.FLOWER
                    ret += 1
                elif board[ny][nx] == g.SOIL:
                    board[ny][nx] = time
                    q.append((ny, nx))
    return ret

def simulate(greens, reds):
    global plate, board, ys, xs, rst

    rq = deque()
    gq = deque()
    visited = [[[False]*2 for _ in range(xs)] for _ in range(ys)]
    for y in range(ys):
        for x in range(xs):
            board[y][x] = plate[y][x]
    for i in reds:
        y, x = i
        visited[y][x][g.RED] = True
        board[y][x] = 2
        rq.append(i)
    for i in greens:
        y, x = i
        visited[y][x][g.GREEN] = True
        board[y][x] = 2
        gq.append(i)

    flower = 0
    time = 3 # 1, -1이 흙과 꽃을 사용됨
    # bfs
    while rq or gq:
        spread(rq, visited, time, g.RED)
        flower += spread(gq, visited, time, g.GREEN)
        time += 1
    rst = max(flower, rst)

def select(cnds, gs, rs):
    for targets in combinations(cnds, gs + rs):
        for greens in combinations(targets, gs):
            reds = [c for c in targets if c not in greens]
            simulate(greens, reds)

select(cnds, gs, rs)
print(rst)
