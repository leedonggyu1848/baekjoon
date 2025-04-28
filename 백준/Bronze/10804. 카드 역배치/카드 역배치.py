def reverse_range(arr, start, end):
    s = start-1
    e = end-1
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

cards = [i+1 for i in range(20)]
for _ in range(10):
    a, b = map(int, input().split())
    reverse_range(cards, a, b)

print(*cards)
