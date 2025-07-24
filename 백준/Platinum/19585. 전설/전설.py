import sys
input = sys.stdin.readline


class Node:
    offset = -ord('a')
    def __init__(self):
        self.next = [None] * 26
        self.is_last = False

    def update(self, s):
        cur = self
        for c in s:
            idx = ord(c) + Node.offset
            if not cur.next[idx]:
                cur.next[idx] = Node()
            cur = cur.next[idx]
        cur.is_last = True


    def find(self, names, target):
        cur = self
        for i in range(len(target)):
            if cur.is_last and target[i:] in names:
                return True
            idx = ord(target[i]) + Node.offset
            if cur.next[idx]:
                cur = cur.next[idx]
            else:
               return False
        return False

c, n = map(int, input().split())
colors = Node()
names = set()

for _ in range(c):
    colors.update(input().rstrip())
for _ in range(n):
    names.add(input().rstrip())

for _ in range(int(input())):
    print("Yes" if colors.find(names, input().rstrip()) else "No")
