import sys

input = sys.stdin.readline

s = []
for _ in range(int(input())):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        s.append(lst[1])
    elif lst[0] == 2:
        if len(s) != 0:
            print(s.pop())
        else:
            print(-1)
    elif lst[0] == 3:
        print(len(s))
    elif lst[0] == 4:
        print(1 if len(s) == 0 else 0)
    elif lst[0] == 5:
        print(s[-1] if len(s) != 0 else -1)
