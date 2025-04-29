k = int(input())
stack = []
for _ in range(k):
    v = int(input())
    if v == 0:
        stack.pop()
    else:
        stack.append(v)

print(sum(stack))
