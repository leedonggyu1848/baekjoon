import sys
import math
input = sys.stdin.readline

n, c = map(int, input().split())
pk = []
rst = 0

for _ in range(int(input())):
    s, e, v = map(int, input().split())
    pk.append((s, e, v))

pk.sort(key=lambda x:(x[1], -x[0]))
slots = [0] * (n+1)

for s, e, v in pk:
    cur_box = math.inf
    for i in range(s, e):
        cur_box = min(cur_box, min(c - slots[i], v))
    rst += cur_box
    for i in range(s, e):
        slots[i] += cur_box

print(rst)
