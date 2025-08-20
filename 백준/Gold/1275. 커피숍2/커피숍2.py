import sys
input = sys.stdin.readline

n, q = map(int, input().split())

tree = [0] * (n * 4)

def left(idx):
    return idx*2+1

def right(idx):
    return idx*2+2

def update(idx, v):
    def inner(li, ri, cur):
        if idx < li or ri < idx:
            return 0
        if li == ri:
            diff = v - tree[cur]
            tree[cur] += diff
            return diff
        mid = (li + ri) // 2
        diff = inner(li, mid, left(cur)) + inner(mid+1, ri, right(cur))
        tree[cur] += diff
        return diff
    inner(0, n, 0)

# lo li ri hi
def search(lo, hi):
    def inner(li, ri, cur):
        if hi < li or ri < lo:
            return 0
        if lo <= li and ri <= hi:
            return tree[cur]
        mid = (li + ri) // 2
        return inner(li, mid, left(cur)) + inner(mid+1, ri, right(cur))
    return inner(0, n, 0)

for i, num in enumerate(map(int, input().split())):
    update(i+1, num)

for _ in range(q):
    lo, hi, idx, v = map(int, input().split())
    print(search(min(lo, hi), max(lo, hi)))
    update(idx, v)
