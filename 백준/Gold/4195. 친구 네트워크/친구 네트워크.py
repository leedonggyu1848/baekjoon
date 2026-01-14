import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(n):
    words = {}
    num = 0
    cnt = [1] * 200001
    p = [-1] * 200001
    def find(v):
        pv = p[v]
        if pv < 0:
            return v
        p[v] = find(pv)
        return p[v]

    def uni(v1, v2):
        pv1 = find(v1)
        pv2 = find(v2)
        if pv1 == pv2:
            return cnt[pv1]
        cnt[pv1] += cnt[pv2]
        p[pv2] = pv1
        return cnt[pv1]

    def get(w):
        nonlocal num
        n = words.get(w, num)
        if n == num:
            words[w] = num
            num += 1
        return n

    for _ in range(n):
        w1, w2 = input().split()
        idx1 = get(w1)
        idx2 = get(w2)
        print(uni(idx1, idx2))

for _ in range(int(input())):
    solve(int(input()))
