import sys
from collections import deque

dire = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

loop = int(sys.stdin.readline())
n = 0

def is_range(y, x):
    global n
    if y < 0 or y >= n:
        return False
    if x < 0 or x >= n:
        return False
    return True

for _ in range(loop):
    rst = 0
    n = int(sys.stdin.readline())
    cur_y, cur_x = [int(v) for v in sys.stdin.readline().split()]
    tar_y, tar_x = [int(v) for v in sys.stdin.readline().split()]
    visited = [[False] * n for _ in range(n)]
    visited[cur_y][cur_x] = True
    q = deque()
    q.append((cur_y, cur_x))
    cur_cnt = 1
    next_cnt = 0
    while q:
        cur_y, cur_x = q[0]
        if cur_y == tar_y and cur_x == tar_x:
            break
        q.popleft()
        cur_cnt -= 1
        for dy, dx in dire:
            next_y = cur_y + dy
            next_x = cur_x + dx
            if is_range(next_y, next_x) and not visited[next_y][next_x]:
                q.append((next_y, next_x))
                visited[next_y][next_x] = True
                next_cnt += 1
        if cur_cnt == 0:
            rst += 1
            cur_cnt, next_cnt = next_cnt, 0
    print(rst)

