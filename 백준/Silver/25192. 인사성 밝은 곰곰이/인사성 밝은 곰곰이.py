N = int(input())
S = set()

cnt = 0
for _ in range(N):
    s1 = input()
    if s1 == "ENTER":
        S = set()
        S.add(s1)
    elif s1 not in S and "ENTER" in S:
        S.add(s1)
        cnt += 1
print(cnt)
