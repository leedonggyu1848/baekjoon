import sys
input = sys.stdin.readline

m = []

for _ in range(5):
    m.append(input().strip())


visited = [[False] * 5 for _ in range(5)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
cur = []
s = set()
def dfs(depth, cnt_y):
    if cnt_y >= 4:
        return
    if depth == 7:
        s.add(tuple(sorted(cur)))
        return
    for y, x in cur:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                visited[ny][nx] = True
                cur.append((ny, nx))
                dfs(depth+1, cnt_y + (m[ny][nx] == 'Y'))
                cur.pop()
                visited[ny][nx] = False

for y in range(5):
    for x in range(5):
        visited[y][x] = True
        cur.append((y, x))
        dfs(1, 0 + (m[y][x] == 'Y'))
        cur.pop()
        visited[y][x] = False
print(len(s))
