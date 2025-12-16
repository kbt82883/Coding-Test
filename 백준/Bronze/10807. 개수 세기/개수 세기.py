n = int(input())
arr = list(map(int, input().split()))
v = int(input())

res = 0
for i in range(n):
    if arr[i]==v:
        res += 1
print(res)