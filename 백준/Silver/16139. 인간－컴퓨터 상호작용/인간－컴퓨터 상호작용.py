import sys

input = sys.stdin.readline

S = input()
q = int(input())

for _ in range(q):
    lst = input().split()
    a = lst[0]
    l, r = map(int, lst[1:3])

    sum_lst = [0]
    for x in range(len(S)):
        if S[x] == a:
            sum_lst.append(sum_lst[-1] + 1)
        else:
            sum_lst.append(sum_lst[-1])

    print(sum_lst[r + 1] - sum_lst[l])
