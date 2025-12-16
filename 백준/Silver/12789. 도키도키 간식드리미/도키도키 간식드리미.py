N = int(input())
S = []
lst = list(map(int, input().split()))
need = 1
for x in lst:
    if x == need:
        need += 1
    else:
        S.append(x)

    while S and S[-1] == need:
        S.pop()
        need += 1

print("Nice" if need== N+1 else "Sad")
