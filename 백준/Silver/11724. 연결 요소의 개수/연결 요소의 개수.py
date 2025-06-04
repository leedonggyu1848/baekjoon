import sys
input = sys.stdin.readline

p = [-1] * 1001

def find(v1):
    global p
    if p[v1] < 0:
        return v1
    p[v1] = find(p[v1])
    return p[v1]

def union(v1, v2):
    global p
    small = find(v1)
    big = find(v2)
    if small == big:
        return False
    if p[small] == p[big]:
        p[small] -= 1
    if p[small] > p[big]:
        small, big = big, small
    p[big] = small
    return True

n, m = map(int, input().split())
for _ in range(m):
    v1, v2 = map(int, input().split())
    union(v1, v2)

rst = 0
for i in p[1:n+1]:
    if i < 0:
        rst += 1
print(rst)
