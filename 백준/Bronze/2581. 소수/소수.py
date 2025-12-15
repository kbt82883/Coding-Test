M = int(input())
N = int(input())

lst = []
for k in range(M, N + 1):
    if k<2:
        continue

    is_decimal = True
    for i in range(2, k // 2 + 1):
        if k % i == 0:
            is_decimal = False
    if is_decimal:
        lst.append(k)
if len(lst) > 0:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)
