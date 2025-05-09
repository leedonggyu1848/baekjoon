import sys
input = sys.stdin.readline

def diff_idx(a, b):
    if a < b:
        a, b = b, a
    return a - b - 1

def cal_max_rect(rects, n, rst, rect_iter, step):
    s = []
    for i in rect_iter:
        while s and s[-1][1] > rects[i]:
            rst[s[-1][0]] += s[-1][1] * diff_idx(i, s[-1][0])
            s.pop()
        s.append((i,rects[i]))
    while s:
        rst[s[-1][0]] += s[-1][1] * diff_idx(i+step, s[-1][0])
        s.pop()

while True:
    n, *rects = map(int, input().split())
    if n == 0:
        break
    rst = rects[:]
    cal_max_rect(rects, n, rst, range(0, n), 1)
    cal_max_rect(rects, n, rst, range(n-1, -1, -1), -1)
    print(max(rst))


