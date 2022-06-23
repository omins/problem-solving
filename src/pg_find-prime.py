# 소수 찾는 함수
# 각 숫자 조합해서 결과 나기

from itertools import permutations
numbers = "011"


num_lst = []
cnt = 0

for i in range(1, len(numbers) + 1):
    for j in permutations(numbers, i):
        s = ''.join(j)
        if 1 < int(s) not in num_lst:
            num_lst.append(int(s))

for num in num_lst:
    prime = True
    for j in range(2, num-1):
        if num % j == 0:
            prime = False
            break
    if prime:
        cnt += 1

print(cnt)
