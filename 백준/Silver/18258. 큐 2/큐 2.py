import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0].startswith("push"):
        v = int(cmd[1])
        q.appendleft(v)
    elif cmd[0].startswith("pop"):
        print(q.pop() if q else -1)
    elif cmd[0].startswith("size"):
        print(len(q))
    elif cmd[0].startswith("empty"):
        print(0 if q else 1)
    elif cmd[0].startswith("front"):
        print(q[-1] if q else -1)
    elif cmd[0].startswith("back"):
        print(q[0] if q else -1)

