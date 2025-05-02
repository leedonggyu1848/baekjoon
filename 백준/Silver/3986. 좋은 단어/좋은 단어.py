import sys

def check_line(line):
    s = []
    for c in line:
        if not s:
            s.append(c)
            continue
        if s[-1] == c:
            s.pop()
        else:
            s.append(c)
    if s:
        return False
    return True

n = int(sys.stdin.readline())
ret = 0
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    if check_line(line):
        ret += 1

print(ret)
