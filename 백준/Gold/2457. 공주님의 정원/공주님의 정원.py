import sys

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cal_days(month, day):
    ret = day
    for i in range(month-1):
        ret += days[i]
    return ret

n = int(sys.stdin.readline())
date = []
flowers = [0] * 366
start = cal_days(3,1)
end = cal_days(12,1)
for _ in range(n):
    s1, s2, e1, e2 = tuple(map(int, sys.stdin.readline().split()))
    s = cal_days(s1, s2)
    e = cal_days(e1, e2)
    if s < start and e <= start:
        continue
    if end <= s and end < e:
        continue
    s = max(s, start)
    e = min(e, end)
    date.append((s, e))
    for i in range(s, e):
        flowers[i] += 1

date.sort()
cur_last = start
next_last = -1
rst = 0
for d in date:
    s, e = d
    while s > cur_last:
        if next_last == -1:
            print(0)
            exit(0)
        rst += 1
        cur_last = next_last
        next_last = -1
    if e > cur_last:
        next_last = max(next_last, e)

if next_last != -1:
    rst += 1
    cur_last = next_last
if cur_last < end:
    print(0)
else:
    print(rst)
