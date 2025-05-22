import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
paint = [[' '] * (n*2-1) for i in range(n)]

def last_draw(pos):
    y, x = pos
    for dx in range(5):
        paint[y][x+dx] = '*'
    paint[y+1][x+1] = '*'
    paint[y+1][x+3] = '*'
    paint[y+2][x+2] = '*'

def draw(pos, height):
    if height == 3:
        last_draw(pos)
        return
    width = height*2-1
    half_w = width >> 1
    half_h = height >> 1
    draw(pos, half_h)
    draw((pos[0], pos[1]+half_w+1), half_h)
    draw((pos[0]+half_h, pos[1]+half_w - (half_w>>1)), half_h)

draw((0,0), n)

for i in paint[::-1]:
    print(''.join(i))

