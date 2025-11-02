import sys
input = sys.stdin.readline

n, m = map(int, input().split())

p = [-1] * (n + 1)

def find(a):
    if p[a] == -1:
        return a
    p[a] = find(p[a])
    return p[a]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa == pb:
        return False
    p[pa] = pb
    return True

for i in map(int, input().split()[1:]):
    union(0, i)

parties = []
for _ in range(m):
    members = list(map(int, input().split()[1:]))
    parties.append(members)
    if len(members) < 2:
        continue
    for member in members:
        union(members[0], member)

rst = 0
root = find(0)
for party in parties:
    for member in party:
        if root != find(member):
            rst += 1
            break
print(rst)
