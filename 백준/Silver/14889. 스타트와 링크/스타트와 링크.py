import sys

input = sys.stdin.readline


def dfs(idx, cnt):
    global ans

    if cnt == N // 2:
        team1 = []
        team2 = []

        for i in range(N):
            if visited[i]:
                team1.append(i)
            else:
                team2.append(i)

        stat1 = 0
        stat2 = 0
        for i in range(N // 2):
            for j in range(i, N // 2):
                a, b = team1[i], team1[j]
                c, d = team2[i], team2[j]

                stat1 += S[a][b] + S[b][a]
                stat2 += S[c][d] + S[d][c]
        ans = min(ans, abs(stat1 - stat2))
        return
    
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            dfs(i+1,cnt+1)
            visited[i] = False


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N
ans = float("inf")

dfs(0, 0)
print(ans)
