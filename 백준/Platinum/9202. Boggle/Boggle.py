import sys
input = sys.stdin.readline

ordA = ord('A')
class node:
    def __init__(self):
        self.last = False
        self.next = [None] * 26

def update(root, s):
    cur = root
    for c in s:
        o = ord(c) - ordA
        if not cur.next[o]:
            cur.next[o] = node()
        cur = cur.next[o]
    cur.last = True

dy = [0, 0, -1, 1, 1, -1, 1, -1]
dx = [-1, 1, 0, 0, 1, -1, -1, 1]
def is_range(y, x):
    return 0 <= y < 4 and 0 <= x < 4
score_board = [0, 0, 0, 1, 1, 2, 3, 5, 11]
def solve(board, root):
    visited = [[False] * 4 for _ in range(4)]
    longest = ""
    cnt = 0
    score = 0

    def dfs(cur, y, x, s):
        global ans
        nonlocal longest, cnt, score
        if len(s) == 9:
            return
        if cur.next[board[y][x]] == None:
            return
        cur = cur.next[board[y][x]]
        s.append(board[y][x])
        if cur.last:
            tmp = "".join(map(lambda x : chr(x+ordA), s))
            if not tmp in ans:
                ans.add(tmp)
                cnt += 1
                score += score_board[len(tmp)]
                if len(longest) < len(tmp):
                    longest = tmp
                elif len(longest) == len(tmp):
                    longest = min(longest, tmp)
        for i in range(len(dy)):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_range(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(cur, ny, nx, s)
                visited[ny][nx] = False
        s.pop()
    for y in range(4):
        for x in range(4):
            visited[y][x] = True
            dfs(root, y, x, [])
            visited[y][x] = False
    return score, longest, cnt


root = node()
for _ in range(int(input())):
    update(root, input().rstrip())
input()

for _ in range(int(input())):
    board = [[] for _ in range(4)]
    for i in range(4):
        for c in input().rstrip():
            board[i].append(ord(c) - ordA)
    ans = set()
    print(*solve(board, root))
    input()

