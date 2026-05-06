def solution(triangle):
    n = len(triangle)

    dp = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]

    for i in range(1, n):
        for j in range(len(triangle[i])):
            # 맨 왼쪽
            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            # 맨 오른쪽
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            # 가운데
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[-1])