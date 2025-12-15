n = int(input())
lstx = []
lsty = []
for _ in range(n):
    x, y = map(int, input().split())
    lstx.append(x)
    lsty.append(y)

lstx.sort()
lsty.sort()

if len(lstx) <= 1:
    print(0)
else:
    size = (lstx[-1] - lstx[0]) * (lsty[-1] - lsty[0])
    print(size)
