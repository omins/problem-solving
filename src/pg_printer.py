from collections import deque


def solution(priorities, location):
    order = []

    papers = [[chr(65 + i), priorities[i]] for i in range(len(priorities))]
    q = deque(papers)

    while q:
        paper, priority = q.popleft()
        if not q:
            order.append(paper)
            break

        for i in range(len(q)):
            if priority < q[i][1]:
                q.append([paper, priority])
                break
        if q[len(q)-1][0] != paper:
            order.append(paper)

    answer = order.index(chr(65-location)) + 1
    return answer
