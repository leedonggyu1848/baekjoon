from collections import deque

def rotate(left_q, mid_qs, right_q):
    mid_qs[0].appendleft(left_q.popleft())
    right_q.appendleft(mid_qs[0].pop())
    mid_qs[-1].append(right_q.pop())
    left_q.append(mid_qs[-1].popleft())
    
def shift(left_q, mid_qs, right_q):
    left_q.appendleft(left_q.pop())
    mid_qs.appendleft(mid_qs.pop())
    right_q.appendleft(right_q.pop())

def solution(rc, operations):
    left_q = deque()
    right_q = deque()
    for y in range(len(rc)):
        left_q.append(rc[y][0])
        right_q.append(rc[y][-1])
    mid_qs = deque()
    for y in range(len(rc)):
        mid_q = deque()
        for x in range(1, len(rc[0]) - 1):
            mid_q.append(rc[y][x])
        mid_qs.append(mid_q)
    
    for operation in operations:
        if operation == "Rotate":
            rotate(left_q, mid_qs, right_q)
        else:
            shift(left_q, mid_qs, right_q)
            
    y = 0
    x = 0
    while mid_qs:
        x = 0
        rc[y][x] = left_q.popleft()
        x += 1
        mid_q = mid_qs.popleft()
        while mid_q:
            rc[y][x] = mid_q.popleft()
            x += 1
        rc[y][x] = right_q.popleft()
        y += 1
    return rc
