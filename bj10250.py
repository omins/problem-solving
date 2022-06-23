t = int(input())
for _ in range(t):
    hotel = []
    h, w, n = map(int, input().split())
    for i in range(1, h + 1):  # 1층 부터
        for j in range(1, w + 1):  # 각 방
            if j < 10:
                room = (j, str(i) + '0' + str(j))  # (걷는 거리, 호수)
                hotel.append(room)
            else:
                room = (j, str(i) + str(j)) # 걷는 거리가 짧은 순으로 정렬
                hotel.append(room)
    hotel.sort(key=lambda x: x[0])
    print(hotel[n-1][1])
