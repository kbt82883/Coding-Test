from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
    a = list(input().split())
    if a[0] == "push":
        q.append(a[1])
    if a[0] == "pop":
        print(q.popleft() if q else -1)
    if a[0] == "size":
        print(len(q))
    if a[0] == "empty":
        print(0 if q else 1)
    if a[0] == "front":
        print(q[0] if q else -1)
    if a[0] == "back":
        print(q[-1] if q else -1)
