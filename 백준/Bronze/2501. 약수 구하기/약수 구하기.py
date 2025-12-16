N, K = map(int, input().split())
lst = []
for i in range(1, N + 1):
    if N % i == 0:
        lst.append(i)

print(lst[K - 1] if len(lst) >= K != -1 else 0)
