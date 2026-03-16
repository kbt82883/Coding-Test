import sys

input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))

M = int(input())
lst = list(map(int, input().split()))

for x in lst:
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == x:
            print(1)
            break
        elif A[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    else:
        print(0)
