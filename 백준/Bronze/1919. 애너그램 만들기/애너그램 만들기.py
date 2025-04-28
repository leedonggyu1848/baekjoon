a = input()
b = input()

counter = [0 for i in range(26)]

for c in a:
    counter[ord(c) - ord('a')] -= 1
for c in b:
    counter[ord(c) - ord('a')] += 1
print(sum(map(abs, counter)))
