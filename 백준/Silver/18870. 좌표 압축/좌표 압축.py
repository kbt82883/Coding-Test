import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

su = sorted(set(lst))

dic = {v: i for i, v in enumerate(su)}

res = [dic[x] for x in lst]
print(*res)
