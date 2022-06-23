def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]

    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in lost:
            _lost.remove(b)

    answer = n - len(_lost)
    return answer


# if stud in reserve:
#             answer += 1
#             reserve.remove(stud)
#             continue
#         if (stud - 1) > 0 and stud-1 in reserve:
#             answer += 1
#             reserve.remove(stud-1)
#             continue
#         if (stud + 1) < n+1 and stud+1 in reserve:
#             answer += 1
#             reserve.remove(stud+1)
#             continue
