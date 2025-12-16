a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 > c:
    print(0)
elif a1 == c:
    print(1 if a2 <= 0 else 0)
else:
    if a1*n0+a2>c*n0:
        print(0)
    else:
        print(1)
