def merge_sort(lst, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q, r)


def merge(lst, p, q, r):
    global cnt
    global flag
    tmp = []
    i = p
    j = q + 1

    while i <= q and j <= r:
        if lst[i] <= lst[j]:
            tmp.append(lst[i])
            i += 1
        else:
            tmp.append(lst[j])
            j += 1
    while i <= q:
        tmp.append(lst[i])
        i += 1
    while j <= r:
        tmp.append(lst[j])
        j += 1
    for idx in range(len(tmp)):
        lst[p + idx] = tmp[idx]
        cnt += 1
        if cnt == K:
            print(tmp[idx])
            flag = False


N, K = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
flag = True
res = merge_sort(lst, 0, len(lst) - 1)
if flag:
    print(-1)
