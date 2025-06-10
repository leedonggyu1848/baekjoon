D, L, R, U = 0, 1, 2, 3
def cal_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def solution(n, m, y, x, c, r, k):
    if (k - cal_dist((y, x), (c, r))) < 0 or (k - cal_dist((y, x), (c, r))) % 2:
        return 'impossible'
    y -= 1
    x -= 1
    c -= 1
    r -= 1
    dy = [1, 0, 0, -1]
    dx = [0, -1, 1, 0]
    ch = ['d', 'l', 'r', 'u']
    answer = []
    
    def go_dir(d, cnt):
        nonlocal y, x, k, answer
        y += dy[d] * cnt
        x += dx[d] * cnt
        k -= cnt
        answer.extend([ch[d]] * cnt)
    if c > y:
        go_dir(D, c - y)
    while y < n-1 and k - cal_dist((y, x), (c, r)) > 0:
        go_dir(D, 1)
    if r < x:
        go_dir(L, x - r)
    while x > 0 and k - cal_dist((y, x), (c, r)) > 0:
        go_dir(L, 1)
    while k - cal_dist((y, x), (c, r)) > 0:
        go_dir(R, 1)
        go_dir(L, 1)
    go_dir(R, r - x)
    go_dir(U, y - c)
    return ''.join(answer)