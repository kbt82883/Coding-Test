import sys

input = sys.stdin.readline
print = sys.stdout.write

S = input().strip()
q = int(input())

sumLst = [[0] * 26 for _ in range(len(S) + 1)]

for i, ch in enumerate(S):
    sumLst[i + 1] = sumLst[i][:]
    sumLst[i + 1][ord(ch) - ord("a")] += 1

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    a = ord(a) - ord("a")
    print(str(sumLst[r + 1][a] - sumLst[l][a]) + "\n")
