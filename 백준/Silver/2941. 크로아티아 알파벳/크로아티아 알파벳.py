word = input()

wordLen = len(word)

cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro:
    wordLen -= word.count(i)

print(wordLen)
