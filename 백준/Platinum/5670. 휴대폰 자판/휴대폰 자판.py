import sys
input = sys.stdin.readline

class Node:
    offset = -ord('a')
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0
        self.is_last = False

    def update(self, s):
        if not s:
            self.is_last = True
            return
        idx = ord(s[0]) + Node.offset
        if not self.next[idx]:
            self.next[idx] = Node()
            self.cnt += 1
        self.next[idx].update(s[1:])

    def cal(self, cnt, is_root):
        ret = 0
        if self.is_last:
            ret += cnt
        for i in range(26):
            if self.next[i] != None:
                if self.cnt == 1 and not is_root and not self.is_last:
                    ret += self.next[i].cal(cnt, False)
                else:
                    ret += self.next[i].cal(cnt+1, False)
        return ret

while True:
    n = input().rstrip()
    if not n:
        break
    n = int(n)
    root = Node()
    for _ in range(n):
        root.update(input().rstrip())
    rst = root.cal(0, True) / n
    print("{:.2f}".format(round(rst * 100) / 100))

