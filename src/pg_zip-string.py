s = "abcabcabcabcdededededede"
expectedAnswer = 14


def solution(s):

    result = []
    if len(s) == 1:
        return 1
    # 문자열 구분 단위: i
    for i in range(1, (len(s) // 2) + 1):  # 1부터 s의 길이 // 2 단위 동안

        listWord = list(s)

        # 초기화
        newStr = ''
        prev = ''
        cur = ''
        samePool = []
        sameLetter = ''

        for j in range(i):  # 초기값
            cur += listWord.pop(0)

        while True:
            _next = ''
            if cur == '':  # 종료조건
                result.append(len(newStr))
                break

            if len(listWord) >= i:  # listWord에 있는 원소가 단위보다 많거나 같으면
                for k in range(i):
                    _next += listWord.pop(0)
            elif len(listWord) < i and listWord:  # 단위보다 작지만 원소는 있을 때
                while listWord:
                    _next += listWord.pop(0)
            elif not listWord:  # listWord에 원소가 없으면
                _next = ''

            if prev == cur or cur == _next:  # 연속되는 원소
                samePool.append(cur)
                sameLetter = cur
            else:
                newStr += cur

            if samePool and cur != _next:  # 연속되는 원소 끝, 압축
                cnt = samePool.count(sameLetter)
                newStr += str(cnt) + sameLetter
                samePool = []
                sameLetter = ''

            # 다음으로 이동
            prev = cur
            cur = _next
    return min(result)


print(solution(s))
