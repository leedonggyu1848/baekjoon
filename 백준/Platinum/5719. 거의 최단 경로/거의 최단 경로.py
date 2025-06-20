import sys
import math
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def dijkstra(edges, src):
    dist = [math.inf for _ in range(len(edges))]
    prev = [{src} for _ in range(len(edges))]
    pq = []
    dist[src] = 0
    push(pq, (0, src))
    while pq:
        spent, cur = pop(pq)
        if spent != dist[cur]:
            continue
        for nxt, delta in enumerate(edges[cur]):
            if delta == math.inf:
                continue
            cmp = dist[cur] + delta
            if dist[nxt] > cmp:
                dist[nxt] = cmp
                prev[nxt] = {cur}
                push(pq, (dist[nxt], nxt))
            elif dist[nxt] == cmp:
                prev[nxt].add(cur)
    return prev, dist

def solve(nv, ne):
    src, dest = map(int, input().split())
    edges = [[math.inf] * nv for _ in range(nv)]
    for _ in range(ne):
        s, e, p = map(int, input().split())
        edges[s][e] = min(edges[s][e], p)

    prev, dist = dijkstra(edges, src)
    if dist[dest] == math.inf:
        return -1

    visited = [False for _ in range(nv)]
    def del_path(cur):
        nonlocal visited
        if cur == src:
            return
        for pre in prev[cur]:
            edges[pre][cur] = math.inf
            if not visited[pre]:
                visited[pre] = True
                del_path(pre)

    visited[dest] = True
    del_path(dest)
    _, dist = dijkstra(edges, src)
    return -1 if dist[dest] == math.inf else dist[dest]


while True:
    nv, ne = map(int, input().split())
    if nv == 0 and ne == 0:
        break
    print(solve(nv, ne))
