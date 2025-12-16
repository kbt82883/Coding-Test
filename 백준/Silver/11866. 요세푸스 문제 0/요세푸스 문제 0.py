from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
q = deque()
for i in range(1, N + 1):
    q.append(i)

res = []
while len(q) != 0:
    for _ in range(K - 1):
        q.append(q.popleft())
    res.append(q.popleft())

print(f"<{", ".join(map(str,res))}>")
