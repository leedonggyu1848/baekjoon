import heapq
import math
push = heapq.heappush
pop = heapq.heappop

def find_index(lst, v):
    try:
        return lst.index(v) + 1000
    except:
        return v - 1
    
def make_mask(node):
    if node < 1000:
        return 0
    return 1 << node - 1000
    
def solution(n, start, end, roads, traps):
    edges = [[] for _ in range(1010)]
    for s, e, cost in roads:
        s = find_index(traps, s)
        e = find_index(traps, e)
        edges[s].append((cost, e, True))
        if s >= 1000 or e >= 1000:
            edges[e].append((cost, s, False))
    
    start = find_index(traps, start)
    end = find_index(traps, end)
    dist = [[math.inf] * (1 << 10) for _ in range(1010)]
    dist[start][0] = 0
    pq = [(0, start, 0)]
    while pq:
        cost, cur, base_mask = pop(pq)
        if dist[cur][base_mask] != cost:
            continue
        if cur == end:
            return cost
        cur_mask = make_mask(cur)
        for step, nxt, flag in edges[cur]:
            nxt_mask = make_mask(nxt)
            if base_mask & cur_mask:
                flag = not flag
            if base_mask & nxt_mask:
                flag = not flag
            nxt_base_mask = base_mask ^ nxt_mask
            if flag and dist[nxt][nxt_base_mask] > cost + step:
                dist[nxt][nxt_base_mask] = cost + step
                push(pq, (cost+step, nxt, nxt_base_mask))