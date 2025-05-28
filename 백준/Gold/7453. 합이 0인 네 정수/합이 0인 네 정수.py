import sys
from collections import Counter
input = sys.stdin.readline

def solve():
    n = int(input())
    A, B, C, D = [], [], [], []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    left = [a + b for a in A for b in B]
    right = [c + d for c in C for d in D]
    counter = Counter(right)

    result = 0
    for s in left:
        result += counter[-s]

    print(result)

solve()