def dig(a, b):
    return a ** 2 + b ** 2

def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        rst = []
        len_y = abs(startY - y)
        len_x = abs(startX - x)
        sum_x = [x + startX, (m - x) + (m - startX)]
        sum_y = [y + startY, (n - y) + (n - startY)]
        if len_y == 0:
            sum_x = [sum_x[0]] if x > startX else [sum_x[1]]
        if len_x == 0:
            sum_y = [sum_y[0]] if y > startY else [sum_y[1]]
        for i in sum_x:
            rst.append(dig(len_y, i))
        for i in sum_y:
            rst.append(dig(len_x, i))
        answer.append(min(rst))
    return answer