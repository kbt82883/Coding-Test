N = int(input())
S = set(["ChongChong"])

for _ in range(N):
    s1, s2 = input().split()
    if s1 in S or s2 in S:
        S.add(s2)
        S.add(s1)
print(len(S))
