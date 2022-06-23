from itertools import combinations


def solution(number, k):
    res_lst = []

    for i in combinations(list(str(number)), len(number) - k):
        str_num = ''
        for num in i:
            str_num += num
        res_lst.append(int(str_num))

    answer = str(max(res_lst))
    return answer
