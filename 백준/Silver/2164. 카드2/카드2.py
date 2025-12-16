from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
q = deque()
for i in range(1, N + 1):
    q.append(i)

i = 1

while len(q) != 1:
    a = q.popleft()
    if i % 2 == 0:
        q.append(a)
    i += 1

print(q[0])
