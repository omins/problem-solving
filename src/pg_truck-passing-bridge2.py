from collections import deque
# 시간과 다리 길이를 고려하는 데 시간을 씀


def solution(bridge_length, weight, truck_weights):
    q = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    time = 0

    while q:
        time += 1
        q.popleft()
        if trucks and sum(q) + trucks[0] <= weight:
            truck = trucks.popleft()
            q.append(truck)
        elif trucks and sum(q) + trucks[0] > weight:
            q.append(0)
    return time
