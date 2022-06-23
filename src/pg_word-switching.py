from collections import deque, defaultdict


def solution(begin, target, words):
    if target not in words:
        return 0

    dic = defaultdict(int)
    visited = {}
    for word in words:
        visited[word] = False

    q = deque()
    q.append(begin)
    dic[begin] = 0

    while q:
        word = q.popleft()

        for i in range(len(word)):
            list_word = list(word)
            for j in range(97, 123):
                if ord(list_word[i]) == j:
                    continue
                else:
                    list_word[i] = chr(j)
                    temp_word = ''.join(list_word)  # 이부분 숙지
                    if temp_word in words and not visited[temp_word]:
                        dic[temp_word] += dic[word] + 1
                        visited[temp_word] = True
                        q.append(temp_word)

    return dic[target]


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))
