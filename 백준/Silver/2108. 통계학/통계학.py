from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()

cnt = Counter(lst)
if len(cnt) >= 2:
    top2 = cnt.most_common(2)
    if top2[0][1] == top2[1][1]:
        n = top2[1][0]
    else:
        n = top2[0][0]
else:
    n = lst[0]

print(round(sum(lst) / N))
print(lst[N // 2])
print(n)
print(lst[-1] - lst[0])
