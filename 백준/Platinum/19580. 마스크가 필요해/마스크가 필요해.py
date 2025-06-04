import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nconsumer, nstore = map(int, input().split())
budgets = []
stores = []
for _ in range(nconsumer):
    start, end = map(int, input().split())
    budgets.append((start, end))
for _ in range(nstore):
    price, cnt = map(int, input().split())
    stores.append((price, cnt))

stores.sort()
budgets.sort()

i = 0
rst = 0
pq = []
for price, cnt in stores:
    while i < len(budgets) and budgets[i][0] <= price:
        if price <= budgets[i][1]:
            push(pq, budgets[i][1])
        i += 1
    while pq and cnt:
        if price <= pop(pq):
            rst += 1
            cnt -= 1

print(rst)
