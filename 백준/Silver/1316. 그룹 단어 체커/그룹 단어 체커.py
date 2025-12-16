wordCount = int(input())
words = []
for i in range(0, wordCount):
    words.append(input())
for i in words:
    for j in range(1, len(i)):
        if i.index(i[j]) < i.index(i[j - 1]):
            wordCount -= 1
            break

print(wordCount)
