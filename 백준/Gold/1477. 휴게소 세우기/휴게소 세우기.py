import sys
import math
input = sys.stdin.readline

n, m, l = map(int, input().split())
houses = list(map(int, input().split()))
houses.sort()
cur = 0
intervals = []
for house in houses:
    intervals.append(house - cur)
    cur = house
if not intervals:
    intervals.append(l)
else:
    intervals.append(l - house)
    intervals.sort(reverse=True)

def can_make(itv) -> bool:
    cnt = 0
    for interval in intervals:
        cnt += (interval // itv) - (interval % itv == 0)
    return cnt <= m

left = 1
right = l
rst = math.inf
while left <= right:
    mid = (left+right)//2
    if can_make(mid):
        rst = min(rst, mid)
        right = mid-1
    else:
        left = mid+1


print(rst)

