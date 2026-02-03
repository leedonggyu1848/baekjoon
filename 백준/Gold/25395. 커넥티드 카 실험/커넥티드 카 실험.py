import sys
from collections import deque
input = sys.stdin.readline

n, start = map(int, input().split())
start -= 1
cars = list(map(int, input().split()))
weight = list(map(int, input().split()))

left_cars = start-1
right_cars = start+1

def push_cars(q, left, right):
    global left_cars, right_cars
    while 0 <= left_cars and left <= cars[left_cars]:
        q.append(left_cars)
        left_cars -= 1
    while right_cars < n and cars[right_cars] <= right:
        q.append(right_cars)
        right_cars += 1

left, right = cars[start], cars[start]
q = deque()
q.append(start)
rst = []
while q:
    cur = q.popleft()
    rst.append(cur+1)
    left = min(left, cars[cur] - weight[cur])
    right = max(right, cars[cur] + weight[cur])
    push_cars(q, left, right)
print(*sorted(rst))
