import sys
input = sys.stdin.readline

def left(node):
    return (node * 2) + 1
def right(node):
    return (node * 2) + 2

def update(idx, v):
    def inner(lo, hi, node):
        if idx < lo or hi < idx:
            return 0
        if lo == hi:
            diff = v - tree[node]
        else:
            mid = (lo + hi) // 2
            diff = inner(lo, mid, left(node)) + inner(mid+1, hi, right(node))
        tree[node] += diff
        return diff
    inner(0, n+m-1, 0)

def upper(idx):
    def inner(lo, hi, node):
        if hi <= idx:
            return 0
        if idx < lo:
            return tree[node]
        mid = (lo + hi) // 2
        return inner(lo, mid, left(node)) + inner(mid+1, hi, right(node))
    return inner(0, n+m-1, 0)


T = int(input())

for _ in range(T):
    # n: 영화의 수, m: 보려는 영화 수
    n, m = map(int, input().split())
    tree = [0] * ((n + m)*4)
    idxs = [n-i-1 for i in range(n)]
    cur = n
    rst = []
    for i in range(n):
        update(i, 1)
    for i in map(lambda x : int(x)-1, input().split()):
        rst.append(upper(idxs[i]))
        update(idxs[i], 0)
        update(cur, 1)
        idxs[i] = cur
        cur += 1
    print(" ".join(map(str, rst)))

