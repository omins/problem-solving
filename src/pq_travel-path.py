
from collections import defaultdict


tickets = [["ICN", "AAA"], ["ICN", "BBB"], ["BBB", 'ICN']]


def solution(tickets):
    graph = defaultdict(list)
    for key, value in tickets:
        graph[key].append(value)
        graph[key].sort()

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        # 특정 공항에서 출발하는 표가 없거나, 티켓을 다 써버린 경우
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
            print(path)
        else:
            stack.append(graph[top].pop(0))
            print(stack)
    return path[::-1]


print(solution(tickets))
