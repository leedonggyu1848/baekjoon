import sys
from collections import deque

input = sys.stdin.readline

nv, np = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(nv-1):
    v1, v2, dist = map(int, input().split())
    edges[v1].append((v2, dist))
    edges[v2].append((v1, dist))

def bfs(start, target):
    q = deque()
    visited = [False] * (nv+1)
    q.append((start, 0))
    visited[start] = True
    while q:
        cur, dist = q.popleft()
        for nxt, delta in edges[cur]:
            if nxt == target:
                return delta + dist
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, delta + dist))
    return 0

for _ in range(np):
    v1, v2 = map(int, input().split())
    print(bfs(v1, v2))
