s = input()

if '0' not in s or '1' not in s:  # 뒤집을 게 없다면
    print(0)
    exit()

cur_met = s[0]
z_met = 0  # 연속되는 0을 만난 횟수
one_met = 0  # 연속되는 1을 만난 횟수

if cur_met == '0':  # 0으로 시작하면
    z_met = 1
else:  # 1로 시작하면
    one_met = 1


for i in range(len(s)):
    if s[i] == '0' and cur_met == '1':  # 연속되는 1이 끊겼으면
        z_met += 1
        cur_met = s[i]
    if s[i] == '0' and cur_met == '0':  # 연속되는 1이면
        continue

    if s[i] == '1' and cur_met == '0':  # 연속되는 0이 끊겼으면
        one_met += 1
        cur_met = s[i]
    if s[i] == '1' and cur_met == '1':  # 연속되는 1이면
        continue

print(min(z_met, one_met))  # 0, 1 중 더 적은 횟수로 등장한 '연속되는 숫자'를 뒤집기
