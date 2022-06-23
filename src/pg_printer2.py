from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(v, i) for i, v in enumerate(priorities)])

    while len(q):
        item = q.popleft()
        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer += 1  # 순서를 하나씩 더해가면서
            if item[1] == location:  # 내가 찾던 원소인지 확인
                break  # 찾던 원소면 break
    return answer
