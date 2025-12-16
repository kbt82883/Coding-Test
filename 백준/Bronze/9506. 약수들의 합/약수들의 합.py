while True:
    n = int(input())
    if n == -1:
        break
    lst = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
            sum += i
    if n != sum:
        print(f"{n} is NOT perfect.", end="")
    else:
        print(f"{n} = {lst[0]}", end="")
        for i in lst[1:]:
            print(f" + {i}", end="")
    print()
