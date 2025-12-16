from collections import deque
import sys

input = sys.stdin.readline

dq = deque()
N = int(input())
for _ in range(N):
    c = list(map(int, input().split()))
    if c[0] == 1:
        dq.appendleft(c[1])
    if c[0] == 2:
        dq.append(c[1])
    if c[0] == 3:
        print(dq.popleft() if dq else -1)
    if c[0] == 4:
        print(dq.pop() if dq else -1)
    if c[0] == 5:
        print(len(dq))
    if c[0] == 6:
        print(0 if dq else 1)
    if c[0] == 7:
        print(dq[0] if dq else -1)
    if c[0] == 8:
        print(dq[-1] if dq else -1)
