import sys
input = sys.stdin.readline

s = input()
bufa = []
bufs = []
bufn = []

is_add = True
for c in reversed('+' + s):
    if c == '+' or c == '-':
        n = int(''.join(reversed(bufn)))
        bufn = []
        bufs.append(n)
        if c == '-':
            bufa.append(-sum(bufs))
            bufs = []
    else:
        bufn.append(c)
if bufs:
    bufa.append(sum(bufs))
print(sum(bufa))
