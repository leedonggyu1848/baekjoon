import sys
n = int(sys.stdin.readline())
m = []
dir = [(0,1), (1,0), (-1,0), (0,-1), (0,0)]
for _ in range(n):
    bit = 0
    for i, c in enumerate(sys.stdin.readline().split()):
        if c == '0':
            bit |= 1 << i
    m.append(bit)
    
def toggle(cy, cx,tm):
    for dy, dx in dir:
        y = dy+cy
        x = dx+cx
        if (0 <= x < n and
            0 <= y < n):
            tm[y] ^= 1 << x

def all_on(tm):
    bit = (1 << n)-1
    for i in tm:
        if bit != i:
            return False
    return True

rst = sys.maxsize

for f_bit in range((1 << n)):
    tm = m[:]
    cnt = 0

    for i in range(n):
        if f_bit & (1 << i):
            toggle(0, i, tm)
            cnt += 1

    for y in range(1, n):
        for x in range(n):
            if not (tm[y-1] & (1 << x)):
                toggle(y, x,tm)
                cnt += 1
    if all_on(tm):
        rst = min(rst, cnt)

if rst == sys.maxsize:
    print("-1")
else:
    print(rst)
