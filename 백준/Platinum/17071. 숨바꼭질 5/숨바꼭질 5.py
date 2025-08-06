import sys
from collections import deque
input = sys.stdin.readline

MAX_DIST = 500_000
s, t = map(int, input().split())
next_pos = [
    lambda x:x+1,
    lambda x:x-1,
    lambda x:x*2
]

footprint = [[-1]*2 for _ in range(MAX_DIST+1)]
def fill_footprint():
    q = deque()
    q.append((s, 0))
    footprint[s][0] = 0
    while q:
        cur, time = q.pop()
        nxt_time = time+1
        for f in next_pos:
            nxt = f(cur)
            if 0 <= nxt <= MAX_DIST and footprint[nxt][nxt_time%2] == -1:
                q.appendleft((nxt, nxt_time))
                footprint[nxt][nxt_time%2] = nxt_time

fill_footprint()
cur = t
time = 0
while cur <= MAX_DIST:
    clue = footprint[cur][time%2]
    if clue != -1 and clue <= time:
        print(time)
        break
    time += 1
    cur += time
if cur > MAX_DIST:
    print(-1)
