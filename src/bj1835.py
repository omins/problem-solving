from collections import deque
n = int(input())
q = deque()
q.append(n)

# 역순으로 수행해서 배열에 저장
for i in range(n-1, 0, -1):
    q.appendleft(i)
    for j in range(i):
        q.appendleft(q.pop())

print(*q)
