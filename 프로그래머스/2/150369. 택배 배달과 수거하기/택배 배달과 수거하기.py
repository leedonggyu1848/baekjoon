def solution(cap, n, deliveries, pickups):
    pi, di = n-1, n-1
    while di >= 0 and deliveries[di] == 0:
        di -= 1
    while pi >= 0 and pickups[pi] == 0:
        pi -= 1
        
    def go(idx, slot):
        cur_n = cap
        while cur_n != 0 and idx >= 0:
            if slot[idx] > 0:
                step = min(cur_n, slot[idx])
                slot[idx] -= step
                cur_n -= step
            while idx >= 0 and slot[idx] == 0:
                idx -= 1
        return idx
    
    rst = 0
    while pi >= 0 or di >= 0:
        if pi >= 0:
            rst += (max(pi, di)+1) << 1
            di = go(di, deliveries)
            pi = go(pi, pickups)
        elif di >= 0:
            rst += (di + 1) << 1
            di = go(di, deliveries)
        elif pi >= 0:
            rst += (pi + 1) << 1
            pi = go(pi, pickups)
    return rst