import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


n = int(input())
tree = [list() for _ in range(n)]
for i in range(n):
    nums = list(map(int, input().split()))
    src = nums[0] - 1
    for tar, cost in zip(nums[1:-2:2], nums[2: -1:2]):
        tree[src].append((tar-1, cost))

def bfs(start):
    global n
    dist = [-1 for _ in range(n)]
    q = deque()
    q.append((start, 0))
    while q:
        cur, from_start = q.popleft()
        dist[cur] = from_start
        for nxt, cost in tree[cur]:
            if dist[nxt] == -1:
                q.append((nxt, cost+from_start))
    return find_longest(dist)

def find_longest(lst):
    mv = -1
    mi = -1
    for i, v in enumerate(lst):
        if mv < v:
            mi = i
            mv = v
    return mi, mv

longest, _ = bfs(0)
_, rst = bfs(longest)
print(rst)
