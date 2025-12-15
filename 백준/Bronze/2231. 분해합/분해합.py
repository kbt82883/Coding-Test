N = int(input())
res = 0
found = False
for i in range(N):
    sum = i
    digits = i
    while digits != 0:
        sum += digits % 10
        digits //= 10
    if sum == N:
        print(i)
        found = True
        break
if not found:
    print(0)
