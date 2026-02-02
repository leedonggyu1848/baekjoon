import sys
input = sys.stdin.readline

sy, sx = map(int, input().split())

m = []
visited = [False] * 30

for _ in range(sy):
    m.append(input().strip())

y = 0
x = 0
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]

def dfs(y, x):
    rst = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < sy and 0 <= nx < sx:
            if not visited[ord(m[ny][nx]) - ord('A')]:
                visited[ord(m[ny][nx]) - ord('A')] = True
                rst = max(dfs(ny, nx)+1, rst)
                visited[ord(m[ny][nx]) - ord('A')] = False
    return rst

visited[ord(m[0][0]) - ord('A')] = True
print(dfs(0, 0))
