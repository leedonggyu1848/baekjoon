import sys
input = sys.stdin.readline

def left(idx, height):
    return idx + height

def right(idx, height):
    return idx + height + 1

n = int(input())
tree = [0]
for _ in range(n):
    tree.extend(map(int, input().split()))

dp = [-1] * len(tree)

def retreive(idx, height):
    global n, tree, dp
    if dp[idx] != -1:
        return dp[idx]
    if height == n:
        dp[idx] = tree[idx]
        return dp[idx]
    left_idx = left(idx, height)
    right_idx = right(idx, height)
    dp[idx] = max(retreive(left_idx, height+1), retreive(right_idx, height+1)) + tree[idx]
    return dp[idx]

print(retreive(1, 1))

