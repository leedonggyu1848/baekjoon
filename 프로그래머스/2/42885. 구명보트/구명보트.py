def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    ret = 0
    while left <= right:
        if left == right or people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        ret += 1
    return ret