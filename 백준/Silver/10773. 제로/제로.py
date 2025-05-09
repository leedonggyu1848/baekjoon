import sys
input = sys.stdin.readline

k = int(input())
s = []
for _ in range(k):
    n = int(input())
    if n:
        s.append(n)
    else:
        s.pop()
print(sum(s))
