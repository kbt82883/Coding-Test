x, y, w, h = map(int, input().split())

minX = 0
minY = 0
if x < w / 2:
    minX = x
else:
    minX = w - x

if y < h / 2:
    minY = y
else:
    minY = h - y

if minX > minY:
    print(minY)
else:
    print(minX)
