while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    if m < n and n % m == 0:
        print("factor")
    elif m > n and m % n == 0:
        print("multiple")
    else:
        print("neither")
