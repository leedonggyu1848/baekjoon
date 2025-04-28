n = int(input())
arr = sorted(list(map(int, input().split())))
tar = int(input())

s, e = 0, len(arr)-1

ret = 0
while s < e:
    v = arr[s] + arr[e]
    if v == tar:
        ret += 1
        s += 1
    elif v < tar:
        s += 1
    else:
        e -= 1

print(ret)
