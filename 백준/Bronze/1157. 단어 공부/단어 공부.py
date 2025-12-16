word = str.lower(input())

arr = list(word)
arr2 = list(set(arr))

arr3 = []
for i in arr2:
    arr3.append(arr.count(i))

count = 0
for i in arr3:
    if i == max(arr3):
        count += 1

if count >= 2:
    print("?")
else:
    print(str.upper(arr2[arr3.index(max(arr3))]))
