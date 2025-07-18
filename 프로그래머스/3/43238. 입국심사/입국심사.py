def solution(n, times):
    left = 0
    right = 1000000000*1000000000
    def can_made(limit):
        total = 0
        for time in times:
            total += (limit // time)
        return total >= n
    rst = 0
    while left <= right:
        mid = (left + right) // 2
        if can_made(mid):
            rst = mid
            right = mid-1
        else:
            left = mid + 1
    return rst
        
