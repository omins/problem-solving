import heapq


def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    h = []

    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업
        for req, dur in jobs:
            if start < req <= now:
                heapq.heappush(h, (dur, req))

        if len(h) > 0:  # 처리할 작업이 있으면
            dur, req = heapq.heappop(h)
            start = now
            now += dur
            answer += now - req  # 완료시간 - 요청시간 (총 소요 시간)
            i += 1
        else:  # 처리할 작업 없는 경우
            now += 1
    return answer // len(jobs)
