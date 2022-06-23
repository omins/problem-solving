from collections import defaultdict
phone_book = ["9", "125", "123", "126535", "567", "88"]


def solution(phone_book):
    answer = True
    dic = defaultdict(bool)

    # dict에 담고
    for phone in phone_book:
        dic[phone] = True

    for phone in phone_book:
        for i in range(1, len(phone)):
            if dic[phone[:i]]:
                return False
    # 각 번호마다 앞에서부터 slicing 하면서 dict에 해당 번호가 있는지 확인
    # 있으면 return False

    # 없으면
    return answer


print(solution(phone_book))
