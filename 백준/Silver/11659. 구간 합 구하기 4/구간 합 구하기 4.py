import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

sum_lst = [0]
k = 0
for i in lst:
    k += i
    sum_lst.append(k)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_lst[j] - sum_lst[i - 1])
