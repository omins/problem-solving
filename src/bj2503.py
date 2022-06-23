from itertools import permutations
num = list(permutations((1, 2, 3, 4, 5, 6, 7, 8, 9), 3))  # 서로 다른 수의 세 자리 숫자

t = int(input())
for _ in range(t):
    q, strk, ball = map(int, input().split())
    removed = 0  # 중간의 리스트 길이를 변경하기 때문에 필요한 변수
    q = list(str(q))

    for i in range(len(num)):
        sCnt, bCnt = 0, 0
        i -= removed
        for j in range(3):
            q[j] = int(q[j])
            if q[j] in num[i]:  # 질문의 j번 인덱스의 숫자가 num의 i번째 튜플에 있는가
                if j == num[i].index(q[j]):  # 있고, 위치도 같으면 스트라이크 횟수 ++
                    sCnt += 1
                else:  # 위치는 다르지만 있다면 볼 횟수 ++
                    bCnt += 1
        if sCnt != strk or bCnt != ball:  # 질문을 통해 얻은 답변과, 순열을 통해 얻은 스트라이크, 볼 횟수가 다르면
            num.remove(num[i])  # 후보지에서 제외
            removed += 1  # 달라진 리스트 길이를 이해 removed --
print(len(num))  # 다 지우고 남은 선택지 갯수
