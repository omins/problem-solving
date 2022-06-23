from collections import defaultdict

# 경우의 수를 구하는 문제였음


def solution(clothes):
    dic = defaultdict(int)
    for value, key in clothes:
        dic[key] += 1
    cnt = 0
    for value in dic.values():
        cnt *= value + 1
    return cnt-1
