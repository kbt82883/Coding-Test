N = int(input())
lst = [2]

for i in range(1, N + 1):
    lst.append(lst[i - 1] * 2 - 1)
print(lst[N] ** 2)
