import sys
import heapq, math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

nv, ne, s, e = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    a, b, dist, t1, t2 = map(int, input().split())
    edges[a].append((dist, b, t1))
    edges[b].append((dist, a, t2))

q = []
cost = [math.inf] * (nv+1)
push(q, (0, 1)) # time, node
cost[0] = -1
cost[1] = 0

slow = 0.5
fast = 1
def cal_time(dist, v):
    return dist / v
def cal_dist(time, v):
    return time * v
def cvt_int(i):
    if i % 1 == 0:
        return int(i)
    return i

def cal_cost(dist, time, stuck):
    if stuck == 0:
        return time + dist / fast
    p1 = cal_dist(max(s - time, 0), fast)
    time = max(s, time)
    remain = dist - p1
    if remain <= 0:
        return cvt_int(time + cal_time(remain, fast))
    p2 = cal_dist(max(e - time, 0), slow)
    time = max(time, e)
    remain = dist - (p1 + p2)
    delta = cal_time(remain, slow if remain < 0 else fast)
    return cvt_int(time + delta)

while q:
    time, cur = pop(q)
    if cost[cur] < time:
        continue
    for dist, nxt, stuck in edges[cur]:
        nxt_time = cal_cost(dist, time, stuck)
        if cost[nxt] > nxt_time:
            cost[nxt] = nxt_time
            push(q, (nxt_time, nxt))

print(cvt_int(max(cost)))
