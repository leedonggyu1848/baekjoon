import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
adj = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]
def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(8)) % 1000000007 for j in range(8)] for i in range(8)]
def power(m, n):
    if n == 1: return m
    v = power(m, n // 2)
    return mul(mul(v, v), m) if n % 2 else mul(v, v)
print(power(adj, int(input()))[0][0])
