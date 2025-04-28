n, x = tuple(map(int, input().split()))
data = list(map(int, input().split()))

print(' '.join([str(i) for i in data if i < x]))

