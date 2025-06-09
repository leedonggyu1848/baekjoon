import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())
start = None
tars = set()
height = [[0] * n for _ in range(n)]
cand = set()

for y in range(n):
    s = input().rstrip()
    for x in range(n):
        if s[x] == 'P':
            start = (y, x)
        elif s[x] == 'K':
            tars.add((y, x))

left_lo = 1000000
right_hi = 0
left_hi = 1000000
right_lo = 0
for y in range(n):
    for x, v in enumerate(map(int, input().split())):
        cand.add(v)
        height[y][x] = v
        if start == (y, x) or (y, x) in tars:
            left_hi = min(left_hi, v)
            right_lo = max(right_lo, v)
        left_lo = min(left_lo, v)
        right_hi = max(right_hi, v)

cand = sorted(list(cand))
left = cand.index(left_hi)
right = cand.index(right_hi)
left_lo = cand.index(left_lo)
right_lo = cand.index(right_lo)

dy = [0, 0, -1, 1, 1, -1, -1, 1]
dx = [-1, 1, 0, 0, 1, -1, 1, -1]
def bfs(left, right):
    q = deque()
    if not (left <= height[start[0]][start[1]] <= right):
        return False
    q.append(start)
    visited = [[False] * n for _ in range(n)]
    while q:
        y, x = q.popleft()
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n \
                and left <= height[ny][nx] <= right \
                and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))
    for y, x in tars:
        if not visited[y][x]:
            return False
    return True

rst = math.inf
while left_lo <= left and right_lo <= right and left <= right:
    if bfs(cand[left], cand[right]):
        rst = min(cand[right] - cand[left], rst)
        right -= 1
    else:
        left -= 1
print(rst)

