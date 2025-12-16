N, k = map(int, input().split())
lst = sorted(list(map(int, input().split())), reverse=True)

print(lst[k - 1])
