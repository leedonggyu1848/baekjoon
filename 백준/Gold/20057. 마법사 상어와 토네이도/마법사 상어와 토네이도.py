import sys, math
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def left(i):
    return (i + 1) % 4
def right(i):
    return (i - 1 + 4) % 4
def pos(i):
    return (dy[i], dx[i])

def pos_left(i):
    return pos(left(i))
def pos_right(i):
    return pos(right(i))

def pos_left_half(i):
    j = left(i)
    return (dy[i] + dy[j], dx[i] + dx[j])
def pos_right_half(i):
    j = right(i)
    return (dy[i] + dy[j], dx[i] + dx[j])
def combine(f1, f2):
    return lambda x : f1(f2(x))

def is_range(y, x):
    return 0 <= y < n and 0 <= x < n

turns = [
    pos_right,
    pos_right_half,
    pos_right,
    combine(pos_right_half, right),
    pos,
    pos_left_half,
    pos_left,
    combine(pos_left_half, left),
    pos_left
]
step = [ 2, 1, 1, 1, 2, 1, 1, 1, 2 ]
tv = [2, 10, 7, 1, 5, 10, 7, 1, 2]
def tornado(y, x, d):
    total = board[y][x]
    rst = 0
    for i in range(9):
        v = math.floor(total * tv[i]/100)
        dy, dx = turns[i](d)
        ny = y + dy * step[i]
        nx = x + dx * step[i]
        if is_range(ny, nx):
            board[ny][nx] += v
        else:
            rst += v
        board[y][x] -= v
    dy, dx = pos(d)
    ny = y + dy
    nx = x + dx
    if is_range(ny, nx):
        board[ny][nx] += board[y][x]
    else:
        rst += board[y][x]
    board[y][x] = 0

    return rst

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
def solve():
    y = n // 2
    x = n // 2
    step = 1
    cnt = 2
    i = 0
    rst = 0
    while True:
        for _ in range(step):
            y += dy[i]
            x += dx[i]
            if not is_range(y, x):
                return rst
            rst += tornado(y, x, i)
        i = left(i)
        cnt -= 1
        if cnt == 0:
            cnt = 2
            step += 1

print(solve())
