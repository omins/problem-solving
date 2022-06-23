from collections import deque
# 시간과 다리 길이를 고려하는 데 시간을 씀
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]


def solution(bridge_length, weight, truck_weights):
    q = deque([0 for _ in range(bridge_length)])
    time = 0

    while q:
        time += 1
        print(time)
        q.popleft()
        if truck_weights and sum(q) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            q.append(truck)
        elif truck_weights and sum(q) + truck_weights[0] > weight:
            q.append(0)
        print(q)
        print(truck_weights)
    return time


solution(bridge_length, weight, truck_weights)
