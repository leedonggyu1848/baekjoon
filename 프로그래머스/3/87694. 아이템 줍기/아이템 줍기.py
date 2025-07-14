from collections import deque

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
    
def is_range(y, x):
    return 1 <= x <= 100 and 1 <= y <= 100

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[False] * 101 for _ in range(101)] 
    for rect in rectangle:
        sx, sy, ex, ey = rect
        for y in range(sy*2, ey*2+1):
            for x in range(sx*2, ex*2+1):
                board[y][x] = True
                
    for rect in rectangle:
        sx, sy, ex, ey = rect
        for y in range(sy*2+1, (ey*2)):
            for x in range(sx*2+1, (ex*2)):
                board[y][x] = False
                
    q = deque()
    visited = [[False] * 101 for _ in range(101)] 
    q.append((characterY*2, characterX*2, 0))
    visited[characterY*2][characterX*2] = True
    while q:
        y, x, cnt = q.pop()
        if (y, x) == (itemY*2, itemX*2):
            return cnt//2
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_range(ny, nx) and board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = True
                q.appendleft((ny, nx, cnt+1))
        