import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, l = map(int, input().split())
nums = list(map(int, input().split()))

def push(q, e):
# queue내부의 값이 증가하도록 만든다.
# 같은 값이어도 넣는다
    while q and q[-1] > e:
        q.pop()
    q.append(e)

def pop(q, e):
    if q[0] == e:
        q.popleft()

q = deque()
rst = []
for i in range(l):
    push(q, nums[i])
    rst.append(q[0])
for i in range(l, n):
    pop(q, nums[i - l])
    push(q, nums[i])
    rst.append(q[0])
print(*rst)
