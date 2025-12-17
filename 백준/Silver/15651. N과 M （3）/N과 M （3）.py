import sys

input = sys.stdin.readline


def bt(lst):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1, N + 1):
        lst.append(i)
        bt(lst)
        lst.pop()


N, M = map(int, input().split())
lst = []
bt(lst)
