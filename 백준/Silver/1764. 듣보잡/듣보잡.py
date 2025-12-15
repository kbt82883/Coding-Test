N, M = map(int, input().split())
s1 = set()
s2 = set()
for _ in range(N):
    s1.add(input())
for _ in range(M):
    s2.add(input())
lst = sorted(list(s1 & s2))
print(len(lst))
for name in lst:
    print(name)
