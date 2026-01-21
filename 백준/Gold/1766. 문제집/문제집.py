import sys
import heapq
input = sys.stdin.readline
pop = heapq.heappop
push = heapq.heappush

nv, ne = map(int, input().split())

outedges = [[] for _ in range(nv+1)]
indegree = [0 for _ in range(nv+1)]

for _ in range(ne):
    bf, at = map(int, input().split())
    outedges[bf].append(at)
    indegree[at] += 1

q = []
rst = []
def insert(target):
    if indegree[target] == 0:
        push(q, target)

for i in range(1, nv+1):
    insert(i)

while q:
    cur = pop(q)
    rst.append(cur)
    for nxt in outedges[cur]:
        indegree[nxt] -= 1
        insert(nxt)

print(*rst)
