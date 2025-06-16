import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n = int(input())
idx = [[] for _ in range(3)]

def union(p, v1, v2):
    small = find(p, v1)
    big = find(p, v2)
    if small == big:
        return False
    if p[small] == p[big]:
        p[small] -= 1
    elif p[small] > p[big]:
        small, big = big, small
    p[big] = small
    return True

def find(p, v):
    if p[v] < 0:
        return v
    p[v] = find(p, p[v])
    return p[v]

for i in range(n):
    x, y, z = map(int, input().split())
    idx[0].append((x, i))
    idx[1].append((y, i))
    idx[2].append((z, i))

for i in range(3):
    idx[i].sort()

pq = []
for cur in range(n-1):
    nxt = cur+1
    for i in range(3):
        push(pq, (idx[i][nxt][0] - idx[i][cur][0], idx[i][cur][1], idx[i][nxt][1]))

rst = 0
p = [-1 for _ in range(n)]
while pq:
    cost, v1, v2 = pop(pq)
    if union(p, v1, v2):
        rst += cost
print(rst)
