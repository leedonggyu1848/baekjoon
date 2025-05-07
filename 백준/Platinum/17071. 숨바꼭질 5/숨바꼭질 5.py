import sys
from collections import deque

start, target = map(int, input().split())

visited = [[-1] * 2 for _ in range(500_001)]
dire = [-1, 1, 2]

step = 0
q = deque()
pushed = 0
pushing = 0
success = False

def is_range(pos):
    return 0 <= pos <= 500_000

def search():
    global target, visited
    step = 0
    cur = target

    while is_range(cur):
        if visited[cur][step%2] != -1 and visited[cur][step%2] <= step:
            print(step)
            return
        step += 1
        cur = cur + step
    print(-1)

visited[start][0] = 0
step = 0
q.appendleft((start, step))
while q:
    pos, step = q.pop()
    next_step = step + 1
    for d in dire:
        if d == 2:
            next_pos = pos * 2
        else:
            next_pos = pos + d
        if is_range(next_pos) and visited[next_pos][next_step%2] == -1:
            visited[next_pos][next_step%2] = next_step
            q.appendleft((next_pos, next_step))

search()
