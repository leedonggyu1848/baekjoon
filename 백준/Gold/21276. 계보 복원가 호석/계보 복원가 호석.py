import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
names = sorted(input().split())
cache = {name:i for i, name in enumerate(names)}
ideg = [0 for _ in range(k)]
edges = [[] for _ in range(k)]
childs = [[] for _ in range(k)]

for _ in range(int(input())):
    c, p = map(lambda n: cache[n], input().split())
    edges[p].append(c)
    ideg[c] += 1

master = []
for i in range(k):
    if ideg[i] == 0:
        master.append(i)

print(len(master))
print(' '.join(map(lambda x:names[x], master)))

q = deque()
for i in range(k):
    if ideg[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for nxt in edges[cur]:
        ideg[nxt] -= 1
        if ideg[nxt] == 0:
            q.append(nxt)
            childs[cur].append(nxt)

for i in range(k):
    print(names[i], len(childs[i]), *map(lambda x:names[x], sorted(childs[i])))
