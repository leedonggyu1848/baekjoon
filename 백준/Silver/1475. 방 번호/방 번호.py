s = input()
cache = [0 for _ in range(9)]

for c in s:
    i = int(c);
    if i == 9:
        i = 6
    cache[i] += 1

cache[6] = (cache[6]+1) // 2
print(max(cache))
