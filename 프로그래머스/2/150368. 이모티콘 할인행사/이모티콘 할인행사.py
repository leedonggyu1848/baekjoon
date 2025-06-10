def dc(discounts, cur, emoticons, users):
    if cur == len(emoticons):
        plus, rst = 0, 0
        for tar, money in users:
            total = 0
            for i in range(len(emoticons)):
                if tar <= discounts[i]:
                    total += (emoticons[i] // 100) * (100 - discounts[i])
            if total >= money:
                plus += 1
            else:
                rst += total
        return (plus, rst)
    rst = (0, 0)
    for i in [10, 20, 30, 40]:
        discounts[cur] = i
        rst = max(rst, dc(discounts, cur+1, emoticons, users))
    return rst
    
def solution(users, emoticons):
    answer = dc([0 for _ in range(len(emoticons))], 0, emoticons, users)
    return list(answer)