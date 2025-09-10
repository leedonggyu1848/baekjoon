import sys
input = sys.stdin.readline

n, n_fire, loop = map(int, input().split())
fires = []

for _ in range(n_fire):
    y, x, m, step, d = map(int, input().split())
    fires.append((y-1, x-1, m, step, d))

board = [[[] for _ in range(n)] for _ in range(n)]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def nxt_pos(y, x, step, d):
    ny = (y + step * dy[d] + n) % n
    nx = (x + step * dx[d] + n) % n
    return (ny, nx)

for _ in range(loop):
    while fires:
        y, x, m, step, d = fires.pop()
        ny, nx = nxt_pos(y, x, step, d)
        board[ny][nx].append((m, step, d))

    for y in range(n):
        for x in range(n):
            if not board[y][x]:
                continue
            cnt, m, step, d = 0, 0, 0, 0
            while board[y][x]:
                cnt += 1
                _m, _step, _d = board[y][x].pop()
                m += _m
                step += _step
                d += _d % 2
            if cnt == 1:
                fires.append((y, x, m, step, _d))
            else:
                if (m // 5) == 0:
                    continue
                for i in range(4):
                    fires.append((y, x, m//5, step//cnt, (i*2) + (d != cnt and d != 0)))

rst = 0
for fire in fires:
    _, _, m, _, _ = fire
    rst += m
print(rst)
