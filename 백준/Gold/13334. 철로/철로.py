import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

roads = []
targets = set()
for _ in range(int(input())):
    s, e = map(int, input().split())
    if e < s:
        s, e = e, s
    roads.append((s, e))
    targets.add(e)

d = int(input())
roads.sort(key=lambda x : (x[1], x[0]))
targets = sorted(list(targets))
road_i = 0
pq = []
rst = 0
for e in targets:
    s = e - d
    while pq and pq[0][0] < s:
        pop(pq)
    while road_i < len(roads) and roads[road_i][1] <= e:
        if s <= roads[road_i][0]:
            push(pq, roads[road_i])
        road_i += 1
    rst = max(rst, len(pq))
print(rst)
