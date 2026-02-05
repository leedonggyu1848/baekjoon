import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

s = input().rstrip()
if s.startswith("::"):
    s = s[1:]
if s.endswith("::"):
    s = s[:-1]
arr = s.split(':')

rst = []
for i in arr:
    if i == '':
        rst.extend(['0000'] * (8 - len(arr) + 1))
    else:
        rst.append(('0'*(4-len(i))) + i)

print(*rst, sep=':')
