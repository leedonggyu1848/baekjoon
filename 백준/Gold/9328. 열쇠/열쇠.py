import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
m = None
sy = 0
sx = 0

def is_key(c):
    return ord('a') <= ord(c) <= ord('z')

def is_door(c):
    return ord('A') <= ord(c) <= ord('Z')

def is_space(c):
    return c == '.' or c == '$' or is_key(c)

def add_key(keys, c):
    keys[ord(c) - ord('a')] = True

def can_open(keys, c):
    return keys[ord(c) - ord('A')]

def get_num_doc(starts, init_keys):
    rst = 0
    doors = []
    keys = [False] * 26
    visited = [[False] * 100 for _ in range(100)]
    for key in init_keys:
        add_key(keys, key)
    q = deque()

    def one_step(y, x):
        nonlocal rst
        flag = False
        if 0 <= y < sy and 0 <= x < sx and not visited[y][x]:
            visited[y][x] = True
            c = m[y][x]
            if is_key(c):
                add_key(keys, c)
                flag = True
            elif is_door(c):
                doors.append((c, y, x))
                flag = True
            if c == '$':
                rst += 1
            if is_space(c):
                q.append((y, x))
        return flag

    for start_y, start_x in starts:
        one_step(start_y, start_x)

    def next_step():
        nonlocal rst
        flag = False
        while q:
            y, x = q.pop()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                flag |= one_step(ny, nx)
        return flag

    while True:
        tmp = []
        while doors:
            door = doors.pop()
            if can_open(keys, door[0]):
                q.append((door[1], door[2]))
            else:
                tmp.append(door)
        doors = tmp
        if not next_step():
            return rst

    return rst
    
def solve(keys):
    starts = []
    for x in range(sx):
        if m[0][x] != '*':
            starts.append((0, x))
        if m[sy-1][x] != '*':
            starts.append((sy-1, x))
    for y in range(sy):
        if m[y][0] != '*':
            starts.append((y, 0))
        if m[y][sx-1] != '*':
            starts.append((y, sx-1))
    return get_num_doc(starts, keys)

for _ in range(int(input())):
    sy, sx = map(int, input().split())
    m = []
    for _ in range(sy):
        m.append(input().strip())
    keys = input().strip()
    if keys == '0':
        keys = ''
    print(solve(keys))
