S = list(input())

alpha = list("abcdefghijklmnopqrstuvwxyz")

result = []
for i in alpha:
    if i in S:
        result.append(S.index(i))
    else:
        result.append(-1)

a = ""
for i in result:
    a += str(i) + " "

print(a)
