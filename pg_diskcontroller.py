from audioop import avg
import math
import heapq


def solution(jobs):
    h = [(duration, start) for start, duration in jobs]
    heapq.heapify(h)
    cur_time = 0
    times = []

    while h:
        dur, srt = heapq.heappop(h)
        time = cur_time - srt + dur
        cur_time += dur
        times.append(time)

    answer = round(sum(times) / len(times))
    return answer
