def solution(sales, links):
    sales = [0] + sales
    edges = [[] for _ in range(len(sales))]
    for s, e in links:
        edges[s].append(e)

    def cal_node(node):
        c_ins = []
        c_exs = []
        if not edges[node]:
            return (sales[node], 0)
        for edge in edges[node]:
            c_in, c_ex = cal_node(edge)
            c_ins.append(c_in)
            c_exs.append(c_ex)

        sum_c_exs = sum(c_exs)
        p_in = sales[node] + sum_c_exs
        p_ex = sales[node] + sum_c_exs
        for c_in, c_ex in zip(c_ins, c_exs):
            p_ex = min(p_ex, c_in + sum_c_exs - c_ex)
        return (p_in, p_ex)

    return min(cal_node(1))