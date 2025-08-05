import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n, m = map(int, input().split())
nums = list(map(int, input().split()))

pq = []
for i in range(2*m-2):
    push(pq, (-nums[i], i))
left = 0
right = 2*m-2
rst = []
while right < n:
    push(pq, (-nums[right], right))
    right += 1
    rst.append(-pq[0][0])
    while pq and pq[0][1] <= left:
        pop(pq)
    left += 1

print(" ".join(map(str, rst)))
