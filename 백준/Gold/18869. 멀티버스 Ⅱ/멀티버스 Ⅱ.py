import sys
from collections import Counter
import bisect
input = sys.stdin.readline

nspace, nplanet = map(int, input().split())
spaces = []
for _ in range(nspace):
    space = list(map(int, input().split()))
    order = sorted(list(set(space)))
    spaces.append(' '.join([str(bisect.bisect_left(order, i)) for i in space]))

rst = 0
for _, v in Counter(spaces).items():
    if v >= 2:
        rst += v*(v-1) // 2
print(rst)
