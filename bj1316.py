n = int(input())
cnt = 0

for i in range(n):
    word = input()
    cur = ''
    visited = []
    isGroup = True

    for ch in word:
        if ch not in visited and ch != cur:  # 아직 방문하지 않았고, 연속되는 문자가 아니면
            cur = ch  # 연속되는 문자는 현재 문자로 초기화
            visited.append(ch)  # 방문처리
        elif ch in visited and ch == cur:  # 이미 방문했고, 연속되고 있으면
            continue
        elif ch in visited and ch != cur:  # 이미 방문했고, 중간에 다른 문자가 섞여 있으면
            isGroup = False
            break
    if isGroup:
        cnt += 1

print(cnt)
