lstx = [0] * 1001
lsty = [0] * 1001
for _ in range(3):
    x, y = map(int, input().split())
    lstx[x] += 1
    lsty[y] += 1

print(lstx.index(1), lsty.index(1))
