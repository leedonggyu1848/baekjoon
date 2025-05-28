import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

def rotate(quad, clock):
    if clock:
        return quad[3], quad[0], quad[1], quad[2]
    else:
        return quad[1], quad[2], quad[3], quad[0]

def flip(quad):
    return quad[1], quad[0], quad[3], quad[2]

def cal_pos(cur, quad, half):
    if quad == 0:
        return cur
    elif quad == 1:
        return (cur[0], cur[1] + half)
    elif quad == 2:
        return (cur[0] + half, cur[1] + half)
    else:
        return (cur[0] + half, cur[1])

def cal_step(cur, quad, piece):
    if quad == 0:
        return cur
    elif quad == 1:
        return cur - piece
    elif quad == 2:
        return cur - 2*piece
    elif quad == 3:
        return cur - 3*piece

def solve(step, pos, quad, level):
    if level == 1:
        print(pos[0]+1, pos[1]+1)
        return
    half = level >> 1
    piece = half ** 2
    q = step // piece
    nxt_pos = cal_pos(pos, quad[q], half)
    nxt_step = cal_step(step, q, piece)
    if q == 0:
        quad = flip(rotate(quad, True))
    elif q == 3:
        quad = flip(rotate(quad, False))
    solve(nxt_step, nxt_pos, quad, half)

solve(m-1, (0, 0), (0, 1, 2, 3), n)
