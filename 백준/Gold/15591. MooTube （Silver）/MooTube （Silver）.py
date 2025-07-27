import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, q = map(int, input().split())

edges = [[] for _ in range(n)]
cache = [[-1] * (n) for _ in range(n)]

for _ in range(n-1):
    v1, v2, r = map(int, input().split()) 
    v1 -= 1
    v2 -= 1
    edges[v1].append((v2, r))
    edges[v2].append((v1, r))

def find(v, minimum, visited):
    ret = 0
    for nxt, r in edges[v]:
        if not visited[nxt] and r >= minimum:
            visited[nxt] = True
            ret += find(nxt, minimum, visited) + 1
    return ret


for _ in range(q):
    minimum, v = map(int, input().split())
    v -= 1
    visited = [False] * n
    visited[v] = True
    print(find(v, minimum, visited))


