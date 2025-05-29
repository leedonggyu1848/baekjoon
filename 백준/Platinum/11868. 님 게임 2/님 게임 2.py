import sys
input = sys.stdin.readline

input()
rst = 0
for n in map(int, input().split()):
    rst ^= n
print('koosaga' if rst else 'cubelover')
