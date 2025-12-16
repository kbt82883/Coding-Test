from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dq = deque((i + 1, v) for i, v in enumerate(lst))

while dq:
    i, v = dq.popleft()
    print(i, end=" ")

    if not dq:
        break

    if v > 0:
        dq.rotate(-(v - 1))
    else:
        dq.rotate(-v)
