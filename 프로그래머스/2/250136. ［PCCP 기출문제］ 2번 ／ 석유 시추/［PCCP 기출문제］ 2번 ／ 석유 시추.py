import sys
sys.setrecursionlimit(10**9)

s_area = []
area = []
sy, sx = 0, 0

def init(land):
    global area, s_area, sy, sx
    sy = len(land)
    sx = len(land[0])
    area = [[-1] * sx for _ in range(sy)]
    s_area = [0] * (sy * sx)

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(y, x, idx, land):
    global s_area, area
    if area[y][x] != -1 or land[y][x] != 1:
        return
    area[y][x] = idx
    s_area[idx] += 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < sy and 0 <= nx < sx:
            dfs(ny, nx, idx, land)
            
def solution(land):
    init(land)
    nxt_area = 0
    for y in range(sy):
        for x in range(sx):
            if area[y][x] == -1 and land[y][x] == 1:
                dfs(y, x, nxt_area, land)
                nxt_area += 1
    answer = 0
    for x in range(sx):
        cur = 0
        s = set()
        for y in range(sy):
            if area[y][x] >= 0 and not area[y][x] in s:
                s.add(area[y][x])
                cur += s_area[area[y][x]]
        answer = max(answer, cur)
            
    return answer