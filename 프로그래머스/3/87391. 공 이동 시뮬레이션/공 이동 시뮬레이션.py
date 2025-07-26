left = 0
right = 1
up = 2
down = 3
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
    
def solution(sy, sx, y, x, queries):
    
    def flip(t):
        if t == up or t == left:
            return t + 1
        else:
            return t - 1
    
    def move(square, t, gap):
        if not square:
            return None
        start, end = square
        gapy = dy[t] * gap
        gapx = dx[t] * gap
        new_start = (start[0] + gapy, start[1] + gapx)
        new_end = (end[0] + gapy, end[1] + gapx)
        return (new_start, new_end)
    
    def turncate(square):
        if not square:
            None
        start, end = square
        if start[0] >= sy or start[1] >= sx:
            return None
        if end[0] < 0 or end[1] < 0:
            return None
        new_start = (max(start[0], 0), max(start[1], 0))
        new_end = (min(end[0], sy-1), min(end[1], sx-1))
        return (new_start, new_end)
    
    def combine(square1, square2):
        if not square1 or not square2:
            return None
        new_start = min(square1[0], square2[0])
        new_end = max(square1[1], square2[1])
        return (new_start, new_end)
    
    def is_range(pos):
        return 0 <= pos[0] < sy and 0 <= pos[1] < sx
    
    def is_boundary(square, t):
        if not square:
            return False
        start, end = move(square, t, 1)
        return not (is_range(start) and is_range(end))
        
    cur = ((y, x), (y, x))
    for query in reversed(queries):
        t, gap = query
        nxt = move(cur, flip(t), gap)
        if is_boundary(cur, t):
            nxt = combine(cur, nxt)
        nxt = turncate(nxt)
        cur = nxt
        if not cur:
            break
    if not cur:
        return 0
    start, end = cur
    return (end[0] - start[0] + 1) * (end[1] - start[1] + 1)