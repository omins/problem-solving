from collections import deque


def solution(people, limit):
    cnt = 0
    people.sort()
    d = deque(people)

    while len(d) >= 2:
        if d[0] + d[-1] <= limit:
            d.pop()
            d.popleft()
            cnt += 1
        else:
            d.pop()
            cnt += 1
    if d:
        d.pop()
        cnt += 1
    return cnt
