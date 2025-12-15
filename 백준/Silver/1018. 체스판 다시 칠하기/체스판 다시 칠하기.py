N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().strip()))

min_cnt = float("inf")
for i in range(N - 7):
    for j in range(M - 7):
        sum1 = 0
        sum2 = 0
        lst1 = [
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
        ]
        lst2 = [
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
            "BWBWBWBW",
            "WBWBWBWB",
        ]
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if grid[x][y] != lst1[x - i][y - j]:
                    sum1 += 1
                if grid[x][y] != lst2[x - i][y - j]:
                    sum2 += 1
        min_sum = min(sum1, sum2)
        min_cnt = min(min_cnt, min_sum)
print(min_cnt)
