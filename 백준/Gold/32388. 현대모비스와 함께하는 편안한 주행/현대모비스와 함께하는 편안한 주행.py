import sys, math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nodes = [(0, 0)]
nodes.append(tuple(map(int, input().split())))
for _ in range(int(input())):
    nodes.append(tuple(map(int, input().split())))

n = len(nodes)

dist = [[math.inf] * n for _ in range(n)]

def cal_dist(v1, v2):
    a = (v1[0] - v2[0]) ** 2
    b = (v1[1] - v2[1]) ** 2
    return math.sqrt(a + b)

for i in range(n):
    for j in range(i, n):
        if i == j:
            dist[i][j] = 0
            continue
        length = cal_dist(nodes[i], nodes[j]) - 2
        length += (i in (0, 1)) + (j in (0, 1))
        dist[i][j] = max(length, 0)
        dist[j][i] = max(length, 0)

pq = []
ijk = [math.inf] * n
for i in range(n):
    ijk[i] = dist[0][i]
    push(pq, (ijk[i], i))

while pq:
    cost, cur = pop(pq)
    if ijk[cur] < cost:
        continue
    for nxt in range(n):
        if ijk[nxt] > cost + dist[cur][nxt]:
            ijk[nxt] = cost + dist[cur][nxt] 
            push(pq, (cost + dist[cur][nxt], nxt))


print(ijk[1])
