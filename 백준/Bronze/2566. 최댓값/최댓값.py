grid = []
max = -1
x, y = 0, 0
for _ in range(9):
    grid.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if max < grid[i][j]:
            x, y = i, j
            max = grid[i][j]


print(max)
print(x+1, y+1)
