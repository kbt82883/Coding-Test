for _ in range(int(input())):
    C = int(input())
    arr = [25, 10, 5, 1]
    i = 0
    res = [0] * 4
    while i < 4 and C > 0:
        if arr[i] > C:
            i += 1
            continue
        C -= arr[i]
        res[i] += 1
    print(*res)
