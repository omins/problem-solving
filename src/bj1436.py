n = int(input())
six_n = 666
cnt = 0

while True:
    if '666' in str(six_n):
        cnt += 1  # cnt번째 영화
    if cnt == n:  # n번째 영화에 도달 시
        print(six_n)  # 영화 제목 출력
        break
    six_n += 1  # six_n 값을 1씩 증가시키며 666이 들어가는 수를 순차적으로 찾음
