grid = []

for _ in range(5):
    grid.append(list(input().strip()))

for i in range(15):
    for j in range(5):
        try:
            print(grid[j][i], end="")
        except:
            continue
