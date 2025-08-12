import sys
from collections import deque
input = sys.stdin.readline

QUEUE = 0    # n개의 deque list
LIST_2D = 1  # n X n list

class Fish:
    def __init__(self, arr):
        self.n = len(arr)
        self.state = QUEUE
        self.q = deque()
        for v in arr:
            q = deque()
            q.append(v)
            self.q.append(q)

    def get_queue(self):
        if self.state == QUEUE:
            return self.q
        elif self.state == LIST_2D:
            x = 0
            while x < n and self.list[x] != -1:
                y = 0
                q = deque()
                while y < n and self.list[y][x] != -1:
                    q.append(self.list[y][x])
                    y += 1
                self.q.append(q)
                x += 1
            self.state = QUEUE
            return self.q

    def get_2dlist(self):
        if self.state == QUEUE:
            self.list = [[-1] * n for _ in range(n)]
            x = 0
            while self.q:
                y = 0
                q = self.q.popleft()
                while q:
                    v = q.popleft()
                    self.list[y][x] = v
                    y += 1
                x += 1
            self.state = LIST_2D
            return self.list
        elif self.state == LIST_2D:
            return self.list

    def flatten(self):
        lst = self.get_2dlist()
        x = 0
        while x < n and self.list[x] != -1:
            y = 0
            while y < n and self.list[y][x] != -1:
                q = deque()
                q.append(self.list[y][x])
                self.q.append(q)
                y += 1
            x += 1
        self.state = QUEUE

 
def push_minimum(fish):
    qs = fish.get_queue()
    minimum = float('inf')
    for q in qs:
        minimum = min(q[0], minimum)
    for q in qs:
        if q[0] == minimum:
            q.append(q.popleft()+1)

def fold(src, tar):
    while src:
        src_q = src.pop()
        tar_i = 0
        while src_q:
            tar[tar_i].append(src_q.popleft())
            tar_i += 1

def fold_loop(fish):
    qs = fish.get_queue()
    src = [qs.popleft()] # stack
    tar = [qs.popleft()]
    while True:
        fold(src, tar)
        if len(qs) < len(tar[0]):
            break
        src = tar
        tar = []
        for _ in range(len(src[0])):
            tar.append(qs.popleft())
    while tar:
        qs.appendleft(tar.pop())

def balance(fish):
    lst = fish.get_2dlist()
    n = fish.n
    diff = [[0] * n for _ in range(n)]
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(n):
        for x in range(n):
            if lst[y][x] == -1:
                continue
            for dy, dx in delta:
                ny = y + dy
                nx = x + dx
                if not (0 <= ny < n and 0 <= nx < n):
                    continue
                if lst[ny][nx] == -1:
                    continue
                d = abs(lst[y][x] - lst[ny][nx]) // 5
                if lst[y][x] < lst[ny][nx]:
                    diff[ny][nx] -= d
                    diff[y][x] += d
                else:
                    diff[ny][nx] += d
                    diff[y][x] -= d
    for y in range(n):
        for x in range(n):
            lst[y][x] += diff[y][x] // 2

def half_fold(fish):
    qs = fish.get_queue()
    half = len(qs) // 2
    src = []
    tar = []
    q = deque()
    for _ in range(half):
        q.appendleft(qs.popleft()[0])
    src.append(q)
    for _ in range(half):
        tar.append(qs.popleft())
    fold(src, tar)
    half = half // 2
    src, tar = tar[:half], tar[half:]
    tar_i = 0
    for q in reversed(src):
        while q:
            tar[tar_i].append(q.pop())
        tar_i += 1
    while tar:
        qs.appendleft(tar.pop())

def cal_diff(fish):
    qs = fish.get_queue()
    lst = []
    while qs:
        lst.append(qs.popleft())
    minimum = float('inf')
    maximum = -1
    for l in lst:
        minimum = min(l[0], minimum)
        maximum = max(l[0], maximum)
        qs.append(l)
    return maximum - minimum


n, k = map(int, input().split())
fish = Fish(list(map(int, input().split())))

rst = 0
while True:
    if cal_diff(fish) <= k:
        break
    rst += 1
    push_minimum(fish)
    fold_loop(fish)
    balance(fish)
    fish.flatten()
    half_fold(fish)
    balance(fish)
    fish.flatten()
print(rst)
