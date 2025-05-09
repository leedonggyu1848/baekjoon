import sys
input = sys.stdin.readline

n = int(input())
s = []
arr = []

for _ in range(n):
    arr.append(int(input()))
cur = 0
buf = []

def pop():
    global s, arr, cur, buf
    while s:
        if s[-1] != arr[cur]:
            break
        s.pop()
        cur += 1
        buf.append('-')

def push(n):
    global s, buf
    s.append(i)
    buf.append('+')

for i in range(1, n+1):
    push(i)
    pop()

print(*buf, sep='\n') if cur == n else print('NO')

