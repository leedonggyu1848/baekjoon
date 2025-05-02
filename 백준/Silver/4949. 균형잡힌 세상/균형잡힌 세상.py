import sys

def check_line(line):
    s = []
    for c in line:
        if c == '(' or c == '[':
            s.append(c)
        elif c == ')' or c == ']':
            cmp = '(' if c == ')' else '['
            if not s or cmp != s[-1]:
                print('no')
                return
            s.pop()
    if s:
        print('no')
    else:
        print('yes')

while True:
    line = sys.stdin.readline().rstrip()
    if line == ".":
        break
    check_line(line)
