n, k = map(int, input().split())
lst = []

for i in range(1, k+1):
    num = str(n * i)[::-1]
    lst.append(int(num))

print(max(lst))
