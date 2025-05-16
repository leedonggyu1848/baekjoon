import sys
import heapq
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
nums = list(map(int, input().split()))

# nums배열에서 l개의 subsequence들
# 각 subsequence에서 최솟값
pq = []
garbage = []
q = deque()
rst = [-1] * n
for i in range(l):
    heapq.heappush(pq, nums[i])
    q.append(nums[i])
    rst[i] = pq[0]

for i in range(l, n):
    out = q.popleft()
    is_garbage = False
    if pq and pq[0] == out:
        heapq.heappop(pq)
    else:
        is_garbage = True
    while garbage and pq and garbage[0] == pq[0]:
        heapq.heappop(pq)
        heapq.heappop(garbage)
    if is_garbage:
        heapq.heappush(garbage, out)
    heapq.heappush(pq, nums[i])
    q.append(nums[i])
    rst[i] = pq[0]
print(*rst)
