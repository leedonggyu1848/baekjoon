import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
nums = set()
for _ in range(n):
    lst = list(map(int, input().split()))
    board.append(lst)
    nums.update(lst)

maximum = max(nums)
minimum = min(nums)

lo = abs(board[0][0] - board[n-1][n-1])
hi = maximum - minimum

def bfs(left, right) -> bool:

    def is_visitable(y, x):
        if y < 0 or y >= n or x < 0 or x >= n:
            return False

        if board[y][x] > right or board[y][x] < left:
            return False
        return True

    visited = [[False] * n for _ in range(n)]
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]
    q = deque()
    if is_visitable(0, 0) and not visited[0][0]:
        q.append((0, 0))
        visited[0][0] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_visitable(ny, nx) and not visited[ny][nx]:
                if ny == n-1 and nx == n-1:
                    return True
                visited[ny][nx] = True
                q.append((ny, nx))
    return False

rst = math.inf
while lo <= hi: # 두 값의 간격을 기준으로 이진탐색
    mid = (lo + hi) // 2
    found = False
    for left in range(minimum, maximum - mid + 1): # 정해진 간격에서 가능한 모든 범위를 탐색
        if bfs(left, left + mid):
            found = True
            break
    if found: # 찾았으면 간격을 줄임
        rst = min(rst, mid)
        hi = mid - 1
    else:
        lo = mid + 1
print(rst)

