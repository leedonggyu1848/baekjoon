import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

def hanoi(src, mid, tar, n):
    if n == 1:
        print(f"{src} {tar}")
    else:
        hanoi(src, tar, mid, n-1)
        print(f"{src} {tar}")
        hanoi(mid, src, tar, n-1)

print((1 << n) - 1)
hanoi(1, 2, 3, n)
