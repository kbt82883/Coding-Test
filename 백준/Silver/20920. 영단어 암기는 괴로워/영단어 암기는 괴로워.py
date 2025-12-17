from collections import Counter
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
for _ in range(N):
    s1 = input().strip()
    if len(s1) >= M:
        dic[s1] = dic.get(s1, 0) + 1

lst = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for x in lst:
    print(x[0])
