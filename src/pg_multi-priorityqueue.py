import heapq
# maxheap과 minheap을 동시에 다루기 위해선 삽입, 삭제 과정에서 '-'를 잘 써야 함

minheap = []
maxheap = []
operations = ["I 7", "I 5", "I -5", "D -1"]


def solution(operations):
    res = []
    for oper in operations:
        op, num = oper.split()
        num = int(num)
        if op == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)  # 최대힙에서 -
        elif op == 'D' and num == 1:
            if minheap and maxheap:
                # maxheap에서 정수 값을 pop하기 위해 -heapq.heappop()
                minheap.remove(-heapq.heappop(maxheap))
        elif op == 'D' and num == -1:
            if minheap and maxheap:
                # minheap의 값을 maxheap에서 지우기 위해 -heapq.heappop(minheap)
                maxheap.remove(-heapq.heappop(minheap))
    if minheap and maxheap:
        res.append(-heapq.heappop(maxheap))
        res.append(heapq.heappop(minheap))
        return res
    else:
        return[0, 0]


print(solution(operations))
