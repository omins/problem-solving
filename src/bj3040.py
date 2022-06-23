arr = [int(input()) for _ in range(9)]

total = sum(arr)

for i in range(len(arr)):
    if len(arr) == 7:
        break
    for j in range(i + 1, len(arr)):
        a, b = arr[i], arr[j]
        if total - (a + b) == 100:
            arr.remove(a)
            arr.remove(b)
            break

for num in arr:
    print(num)
