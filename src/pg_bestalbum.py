import operator
from collections import defaultdict

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 500, 800, 2500]


def solution(genres, plays):
    gen_rank = defaultdict(int)  # 장르별 순위
    gen_songs = defaultdict(list)
    answer = []

    for i in range(len(genres)):
        gen_rank[genres[i]] += plays[i]  # 장르별 재생횟수 저장
        gen_songs[genres[i]].append([i, plays[i]])  # 장르별 곡 저장
        gen_songs[genres[i]].sort(key=lambda x: (-x[1], x[0]))  # 이부분 숙지

    gen_rank = sorted(gen_rank.items(), key=lambda x: x[1], reverse=True)
    print(gen_songs)
    cnt = 0
    for genre in gen_rank:
        print(genre[0])
        cnt = 0
        for song in gen_songs[genre[0]]:
            print(song)
            answer.append(song[0])
            cnt += 1
            if cnt == 2:
                break
        print(answer)
    return answer


solution(genres, plays)
