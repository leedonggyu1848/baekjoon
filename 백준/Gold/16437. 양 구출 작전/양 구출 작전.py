import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]
node = [None for _ in range(n+1)]
node[1] = ('S', 0)

for i in range(n-1):
    t, a, v2 = input().split()
    v1 = i + 2
    v2 = int(v2)
    node[v1] = (t, int(a))
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False for _ in range(n+1)]
def solve(cur):
    visited[cur] = True
    t, num = node[cur]
    if t == 'S':
        sheep = num
    else:
        sheep = -num
    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        sheep += solve(nxt)
    return max(sheep, 0)

print(solve(1))
