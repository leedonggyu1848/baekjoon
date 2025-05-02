import sys

s = sys.stdin.readline().rstrip()

class Node:
    def __init__(self, v, parrent):
        self.v = v
        self.parrent = parrent
        self.childs = []

    def compact_childs(self):
        if not self.childs:
            return
        child_value = 0
        for child in self.childs:
            child.compact_childs()
            child_value += child.v
        self.childs = []
        self.v *= child_value


brace = []
root = Node(1, None)
cnode = root

def close_brace(c):
    global brace, cnode
    cmp = '(' if c == ')' else '['
    if not brace or brace[-1] != cmp:
        return False
    brace.pop()
    cnode = cnode.parrent
    return True

def open_brace(c):
    global brace, cnode
    v = 2 if c == '(' else 3
    brace.append(c)
    cnode.childs.append(Node(v, cnode))
    cnode = cnode.childs[-1]
    return True

def solve():
    global nums, brace
    for c in s:
        if c == '(' or c ==  '[':
            if not open_brace(c):
                print(0)
                return
        elif c == ')' or c == ']':
            if not close_brace(c):
                print(0)
                return

    if brace:
        print(0)
        return
    root.compact_childs()
    print(root.v)

solve()
