import heapq

scoville = [1, 2, 3, 9, 10, 12]
k = 7


def solution(scoville, k):
    heapq.heapify(scoville)  # heapify는 리턴 값이 없는 함수임
    cnt = 0

    while scoville[0] < k:
        heapq.heappush(scoville, heapq.heappop(
            scoville) + (heapq.heappop(scoville)*2))
        cnt += 1
        # 조건을 확인하는 데서 시간 복잡도가 늘어나고 있었음
        if len(scoville) == 1 and scoville[0] < k:
            return -1
    return cnt


print(solution(scoville, k))
