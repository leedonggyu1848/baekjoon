def cvt_days(year, month, day):
    return (year * 12 * 28) + (month * 28) + day
    
def solution(today, terms, privacies):
    answer = []
    n_year, n_month, n_day = map(int, today.split('.'))
    n_days = cvt_days(n_year, n_month, n_day)
    valid = {}
    for term in terms:
        term, month = term.split()
        valid[term] = int(month) * 28
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        year, month, day = map(int, date.split('.'))
        days = cvt_days(year, month, day)
        diff = n_days - days
        if diff >= valid[term]:
            answer.append(i+1)
    return answer