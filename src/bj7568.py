import sys
input = sys.stdin.readline

n = int(input())
pers = [list(map(int, input().split())) for _ in range(n)]

for x, y in pers:
    cnt = 1
    for p, q in pers:
        if x < p and y < q:
            cnt += 1
    print(cnt, end=' ')
