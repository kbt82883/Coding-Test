def hanoi(n, fr, tmp, to):
    if n == 1:
        arr.append((fr, to))
        return

    hanoi(n - 1, fr, to, tmp)
    arr.append((fr, to))
    hanoi(n - 1, tmp, fr, to)


n = int(input())

arr = []

hanoi(n, 1, 2, 3)

print(len(arr))

for fr,to in arr:
    print(fr, to)
