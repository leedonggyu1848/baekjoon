import sys
from collections import deque
input = sys.stdin.readline

def find(p, v):
    if p[v] < 0:
        return v
    p[v] = find(p, p[v])
    return p[v]

def uni(p, v1, v2):
    pv1 = find(p, v1)
    pv2 = find(p, v2)
    if pv1 == pv2:
        return False
    p[pv1] = pv2
    return True

def kruscal(q, nv):
    ret = 0
    p = [-1] * (nv+1)
    while q:
        v1, v2, color = q.pop()
        if not uni(p, v1, v2):
            continue
        if color == 'B':
            ret += 1
    return ret

while True:
    nv, ne, k = map(int, input().split())
    if (nv, ne, k) == (0, 0, 0):
        break
    q1 = deque()
    q2 = deque()
    for _ in range(ne):
        color, v1, v2 = input().split()
        v1 = int(v1)
        v2 = int(v2)
        if color == 'B':
            q1.appendleft((v1, v2, color))
            q2.append((v1, v2, color))
        else:
            q1.append((v1, v2, color))
            q2.appendleft((v1, v2, color))
    print(1 if kruscal(q1, nv) <= k <= kruscal(q2, nv) else 0)

