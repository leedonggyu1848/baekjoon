import sys
from collections import deque
input = sys.stdin.readline


def push(s, t):
    cur = trie
    for c in s:
        cur['type'] = t
        if c in cur:
            cur = cur[c]
        else:
            cur[c] = {}
            cur = cur[c]
    cur['type'] = t
    cur['end'] = t

def bfs():
    q = deque()
    q.append(trie)
    rst = 0
    while q:
        cur = q.pop()
        if cur['type']:
            rst += 1
        else:
            if cur.get('end', False):
                rst += 1
            for key in cur.keys():
                if key == 'type' or key == 'end':
                    continue
                q.append(cur[key])
    return rst

for _ in range(int(input())):
    trie = {}
    for _ in range(int(input())):
        push(input().rstrip(), True)
    for _ in range(int(input())):
        push(input().rstrip(), False)
    print(bfs())