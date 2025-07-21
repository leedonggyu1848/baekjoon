def solution(gems):
    d = {}
    idx = 0
    left = 0
    right = -1
    for i, gem in enumerate(gems):
        if not gem in d:
            d[gem] = idx
            idx += 1
            right = i
    cnt = {}
    m = right - left
    rst = [left+1, right+1]
    for i in range(right+1):
        cnt[gems[i]] = cnt.get(gems[i], 0) + 1
    while True:
        while cnt[gems[left]] > 1:
            cnt[gems[left]] -= 1
            left += 1
        if m > right - left:
            m = right - left
            rst = [left+1, right+1]
            
        if right == len(gems) - 1:
            break
        right += 1
        cnt[gems[right]] += 1
        
    return rst