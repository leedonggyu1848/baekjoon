import sys
input = sys.stdin.readline

class node:
    def __init__(self):
        self.n = 0
        self.lst = [None] * 26

n = int(input())

def update(root, src):
    cur = root
    rst = []
    completed = False
    for c in src:
        o = ord(c) - ord('a')
        if not completed:
            rst.append(c)
        if cur.lst[o] == None:
            completed = True
            cur.lst[o] = node()
        cur = cur.lst[o]
    cur.n += 1
    if not completed:
        if cur.n != 1:
            rst.append(str(cur.n))
    return "".join(rst)

root = node()
for _ in range(n):
    s = input().rstrip()
    print(update(root, s))