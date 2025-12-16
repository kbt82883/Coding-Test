from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

dq = deque()
for i in range(len(B)):
    if A[i] == 0:
        dq.append(B[i])

for c in C:
    dq.appendleft(c)
    print(dq.pop(), end=" ")
