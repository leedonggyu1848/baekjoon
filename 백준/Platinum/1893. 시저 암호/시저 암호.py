import sys
input = sys.stdin.readline

t = int(input())

def tf_index(seq, plain):
    rst = []
    for i in range(len(plain)):
        rst.append(seq.index(plain[i]))
    return rst

# ti: text index (suffix 제공)
# pi: pattern index (prefix 제공)
def make_failure(s):
    f = [0] * len(s)
    pi = 0
    for ti in range(1, len(s)):
        while pi > 0 and s[pi] != s[ti]: pi = f[pi-1]
        if s[pi] == s[ti]:
            pi += 1
            f[ti] = pi
    return f

for _ in range(t):
    seq = input().rstrip()
    plain = input().rstrip()
    pw = input().rstrip()
    pattern = tf_index(seq, plain)
    f = make_failure(pattern)
    rst = []
    for offset in range(len(seq)):
        pi = 0
        cnt = 0
        for ti in range(len(pw)):
            while pi > 0 and seq[(pattern[pi]+offset) % len(seq)] != pw[ti]: pi = f[pi-1]
            if seq[(pattern[pi]+offset) % len(seq)] == pw[ti]:
                if pi == len(pattern)-1:
                    cnt += 1
                    pi = f[pi]
                else:
                    pi += 1
        if cnt == 1:
            rst.append(offset)
    if len(rst) == 0:
        print('no solution')
    elif len(rst) == 1:
        print('unique:', ' '.join(map(str, rst)))
    else:
        print('ambiguous:', ' '.join(map(str, rst)))


