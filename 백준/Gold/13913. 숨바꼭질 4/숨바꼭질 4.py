import sys
from collections import deque
input = sys.stdin.readline

before = [-1] * 200_001
start,tar = map(int, input().split())
before[start] = start

def is_range(n):
    if n > 200_000 or n < 0:
        return False
    return True

q = deque()
q.append(start)
while q:
    cur = q.popleft()
    if cur == tar:
        break;
    nxts = [cur-1, cur+1, cur*2]
    for nxt in nxts:
        if is_range(nxt) and before[nxt] == -1:
            before[nxt] = cur
            q.append(nxt)

path = []
rst = 0
while before[cur] != cur:
    path.append(cur)
    cur = before[cur]
    rst += 1
path.append(cur)
print(rst)
print(*reversed(path))
