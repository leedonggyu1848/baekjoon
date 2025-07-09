import sys
input = sys.stdin.readline

my, mx, width, k = map(int, input().split())
stars = []
stars_x = []
stars_y = []
for _ in range(k):
    x, y = map(int, input().split())
    stars.append((y, x))
    stars_y.append(y)
    stars_x.append(x)

stars_y = sorted(set(stars_y))
stars_x = sorted(set(stars_x))
n_stars = len(stars)

rst = 0
for y in stars_y:
    for x in stars_x:
        cnt = 0
        for star in stars:
            if y <= star[0] <= y + width and x <= star[1] <= x + width:
                cnt += 1
        rst = max(cnt, rst)

print(n_stars - rst)
