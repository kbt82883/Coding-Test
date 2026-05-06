from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0

    for i in range(n):
        if not visited[i]:
            answer += 1

            q = deque([i])
            visited[i] = True

            while q:
                cur = q.popleft()

                for nxt in range(n):
                    if computers[cur][nxt] == 1 and not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)

    return answer