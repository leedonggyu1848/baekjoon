from collections import deque
import sys
import heapq

n, l = map(int, sys.stdin.readline().split())
nums = tuple(map(int, sys.stdin.readline().split()))

q = deque()
pq = []
included = [False] * n
rst = []

for i, num in enumerate(nums):
    if len(q) == l:
        included[q.popleft()[1]] = False
    q.append((num, i))
    included[i] = True
    heapq.heappush(pq, (num, i))
    while not included[pq[0][1]]:
        heapq.heappop(pq)
    rst.append(pq[0][0])
print(*rst)
