import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

nv, m, ne = map(int, input().split())
items = [0] + (list(map(int, input().split())))
board = [[math.inf] * (nv+1) for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    board[v1][v2] = cost
    board[v2][v1] = cost

for i in range(1, nv+1):
    board[i][i] = 0

for mid in range(nv+1):
    for v1 in range(nv+1):
        for v2 in range(nv+1):
            board[v1][v2] = min(board[v1][mid] + board[mid][v2], board[v1][v2])

rst = 0
for i in range(1, nv+1):
    cur = 0
    for j in range(1, nv+1):
        if board[i][j] <= m:
            cur += items[j]
    rst = max(rst, cur)

print(rst)
