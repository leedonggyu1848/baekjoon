import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

n = int(input())
time_table = []
for _ in range(n):
    s, e = map(int, input().split())
    time_table.append((s, e))

time_table.sort()
cur_list = [0]
rst = 0
for s, e in time_table:
    found = False
    if cur_list[0] <= s:
        pop(cur_list)
    push(cur_list, e)

print(len(cur_list))
