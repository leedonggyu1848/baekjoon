import sys
input = sys.stdin.readline

n = int(input())
lst = [None] * n
for i in range(n):
    s, e = map(int, input().split())
    lst[i] = (s, e)
lst.sort()

cur_s = -1_000_000_001
cur_e = -1_000_000_001
rst = 0
for s, e in lst:
    if cur_e < s:
        rst += cur_e - cur_s
        cur_s = s
    if cur_e < e:
        cur_e = e
rst += cur_e - cur_s
print(rst)
