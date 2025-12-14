arr = list(map(int, input().split()))
cnt = [1, 1, 2, 2, 2, 8]

res = []
for i in range(len(arr)):
    if arr[i] != cnt[i]:
        res.append(cnt[i] - arr[i])
    else:
        res.append(0)

print(*res)
