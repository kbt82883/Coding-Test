arr = list(range(0, 31))

for _ in range(28):
    n = int(input())
    arr[n] = -1

arr.sort()
print(arr[-2])
print(arr[-1])
