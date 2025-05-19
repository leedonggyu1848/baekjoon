import sys
input = sys.stdin.readline

n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())


sum(map(lambda x : (x + t-1) // t, size))
print(sum(map(lambda x : (x + t-1) // t, size)))
print(n // p, n % p)
