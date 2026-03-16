import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

sumlst = [0]
modlst = [0]

for i in range(N):
    sumlst.append(sumlst[i] + lst[i])
    modlst.append(sumlst[i + 1] % M)

cntMod = [0] * M
for x in modlst:
    cntMod[x] += 1

ans = 0
for i in cntMod:
    ans += i * (i - 1) // 2

print(ans)
