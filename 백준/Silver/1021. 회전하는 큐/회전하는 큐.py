import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))
tars = list(map(int, sys.stdin.readline().split()))
nums = deque([i for i in range(1, n+1)])

def left():
    global nums
    nums.rotate(-1)
def right():
    global nums
    nums.rotate(1)

def cal_left(cur, tar):
    global nums
    cnt = 0
    while nums[0] != tar:
        left()
        cnt += 1
    for _ in range(cnt):
        right()
    return cnt

def cal_right(cur, tar):
    global nums
    cnt = 0
    while nums[0] != tar:
        right()
        cnt += 1
    for _ in range(cnt):
        left()
    return cnt

ret = 0
cur = 1

def pop_left(cnt):
    global nums
    for _ in range(cnt):
        left()
    nums.popleft()

def pop_right(cnt):
    for _ in range(cnt):
        right()
    nums.popleft()

for tar in tars:
    lv = cal_left(cur, tar)
    rv = cal_right(cur, tar)
    if lv < rv:
        pop_left(lv)
        ret += lv
    else:
        pop_right(rv)
        ret += rv
print(ret)
