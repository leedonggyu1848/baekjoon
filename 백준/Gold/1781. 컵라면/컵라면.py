import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n = int(input())
stat = []
for _ in range(n):
    day, reward = map(int, input().split())
    stat.append((day, reward))
stat.sort(key=lambda x:(-x[0], -x[1]))

day = stat[0][0]
cur = 0
pq = []

def push_all():
    global cur
    while cur < len(stat) and day <= stat[cur][0]:
        push(pq, -stat[cur][1])
        cur += 1

push_all()
rst = 0
while cur < len(stat):
    if pq:
        rst += -pop(pq)
    day -= 1
    push_all()

while pq and day > 0:
    day -= 1
    rst += -pop(pq)

print(rst)
