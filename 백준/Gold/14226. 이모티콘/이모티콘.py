import sys, math
from collections import deque
input = sys.stdin.readline
q = deque()
n = int(input())
visited = [[math.inf] * 2000 for _ in range(2000)]

def push(time, screen, clip):
    if not (0 <= screen < 2000 and 0 <= clip < 2000):
        return
    if visited[screen][clip] <= time:
        return
    visited[screen][clip] = time
    if not q:
        q.append((time, screen, clip))
        return
    if q[-1][0] < time:
        q.appendleft((time, screen, clip))
    else:
        q.append((time, screen, clip))

push(0, 1, 0)
while True:
    time, screen, clip = q.pop()
    if screen == n:
        print(time)
        break
    push(time+1, screen-1, clip)
    push(time+1, screen+clip, clip)
    push(time+1, screen, screen)
