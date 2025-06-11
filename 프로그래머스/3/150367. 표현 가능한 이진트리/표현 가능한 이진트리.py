def are_not_children_zero(s, idx, cnt):
    if cnt == 0:
        return True
    left = idx - cnt
    right = idx + cnt
    if s[idx] == '0' and (s[left] == '1' or s[right] == '1'):
        return False
    return are_not_children_zero(s, left, cnt // 2) \
			and are_not_children_zero(s, right, cnt // 2)


    
def is_completed(n):
    s = bin(n)[2:]
    cnt = len(s)
    cur = 1
    for _ in range(1, 15):
        cur *= 2
        if cnt <= cur - 1:
            break
    slot = cur - 1
    s = ('0' * (slot - cnt)) + s
    mid = len(s) // 2
    print('start')
    return 1 if are_not_children_zero(s, mid, (mid+1) // 2) else 0
    
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(is_completed(number))
    return answer