import sys
input = sys.stdin.readline

n = int(input())

def next_q(x, row, pdg, ndg):
    rst = 0
    c_row = 1
    c_pdg = 1 << x
    c_ndg = 1 << (x+n)
    for y in range(n):
        if not ((row & c_row) or (pdg & c_pdg) or (ndg & c_ndg)):
            if x == n-1:
                return 1
            else:
                rst += next_q(x+1, row ^ c_row, pdg ^ c_pdg, ndg ^ c_ndg)
        c_row = c_row << 1
        c_pdg = c_pdg << 1
        c_ndg = c_ndg >> 1
    return rst

print(next_q(0, 0, 0, 0))
