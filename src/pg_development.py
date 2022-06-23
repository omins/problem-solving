from collections import deque

progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    q_prog = deque(progresses)
    q_spd = deque(speeds)
    day = 0
    cnt = 0
    answer = []

    while q_prog:
        cnt = 0
        day += 1
        while q_prog and q_prog[0] + (q_spd[0] * day) >= 100:
            q_prog.popleft()
            q_spd.popleft()
            cnt += 1
        if cnt:
            answer.append(cnt)
    return answer


print(solution(progresses, speeds))
