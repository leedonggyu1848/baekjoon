from collections import deque
import sys
input = sys.stdin.readline

nv, ne = map(int, input().split())
s, e = map(int, input().split())
edges = [[] for _ in range(nv+1)]
for _ in range(ne):
    v1, v2, cost = map(int, input().split())
    edges[v1].append((v2, cost))
    edges[v2].append((v1, cost))

def can(w):
    visited = [False] * (nv+1)
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        cur = q.popleft()
        for nxt, cost in edges[cur]:
            if cost >= w and not visited[nxt]:
                if nxt == e:
                    return True
                q.append(nxt)
                visited[nxt] = True
    return False

rst = 0
left = 0
right = 1_000_000
while left <= right:
    mid = (left + right) // 2
    if can(mid):
        rst = max(rst, mid)
        left = mid + 1
    else:
        right = mid - 1

print(rst)
