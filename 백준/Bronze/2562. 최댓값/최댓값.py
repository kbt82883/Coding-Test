arr = []
for _ in range(9):
    arr.append(int(input()))

max = sorted(arr)[-1]

for i in range(9):
    if arr[i] == max:
        print(arr[i])
        print(i + 1)
