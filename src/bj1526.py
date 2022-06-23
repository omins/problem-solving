n = int(input())
nums = []

for i in range(1, n + 1):
    newI = str(i)
    isGM = True
    for ch in newI:
        if ch in ('0', '1', '2', '3', '5', '6', '8', '9'):
            isGM = False
            break
    if isGM:
        nums.append(i)

print(max(nums))
