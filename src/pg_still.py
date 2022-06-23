def solution(money):
    # 집이 3개일 경우
    if len(money) == 3:
        return max(money)

    # 집이 4개일 경우
    if len(money) == 4:
        return max(money[0] + money[2], money[1] + money[3])

    pick_front = 0
    pick_behind = 0

    # 앞에 집 터는 경우 (뒤에 집 못 턴다.)
    d = [0 for _ in range(len(money))]
    d[0] = money[0]
    d[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        d[i] = max(d[i-2] + money[i], d[i-1])

    pick_front = max(d)

    # 뒤에 집 터는 경우
    d = [0 for _ in range(len(money))]

    d[0] = 0
    d[1] = money[1]

    for i in range(2, len(money)):
        d[i] = max(d[i-2] + money[i], d[i-1])

    pick_behind = max(d)

    answer = max(pick_front, pick_behind)
    return answer
