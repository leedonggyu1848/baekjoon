import sys, math
input = sys.stdin.readline

nv, ne, start, dest = map(int, input().split())
board = [[math.inf] * (nv+1) for _ in range(nv+1)]
for _ in range(ne):
    s, e, cost = map(int, input().split())
    board[s][e] = min(board[s][e], cost)
for i in range(1, nv+1):
    board[i][i] = 0

for mid in range(1, nv+1):
    for s in range(1, nv+1):
        for e in range(1, nv+1):
            board[s][e] = min(board[s][e], board[s][mid] + board[mid][e])

def get_options(q):
    return [
        board[start][dest],
        board[start][q[0]] + q[2] + board[q[1]][dest],
        board[start][q[3]] + q[5] + board[q[4]][dest],
        board[start][q[0]] + q[2] + board[q[1]][q[3]] + q[5] + board[q[4]][dest],
        board[start][q[3]] + q[5] + board[q[4]][q[0]] + q[2] + board[q[1]][dest],
    ]
for _ in range(int(input())):
    rst = min(get_options(list(map(int, input().split()))))
    print(-1 if rst == math.inf else rst)
