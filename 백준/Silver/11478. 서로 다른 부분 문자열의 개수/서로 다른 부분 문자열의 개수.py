S = input()
s = set()

for size in range(1, len(S) + 1):
    for l in range(len(S)):
        s.add(S[l : l + size])

print(len(s))
