import sys
from itertools import starmap
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

# (index, count) list
# count: 같은 높이인 원소가 연속적으로 몇개가 있는가
s = []
rst = 0

for h in arr:
    while s and s[-1][0] < h:
        rst += 1
        s.pop()
    is_same = s and s[-1][0] == h
    if s:
        rst += s[-1][1]+(len(s)!=s[-1][1]) if is_same else 1
    s.append((h, s[-1][1]+1 if is_same else 1))

print(rst)
