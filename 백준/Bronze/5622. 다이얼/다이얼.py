s = input()
arr = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

res = 0
for char in s:
    for i in range(len(arr)):
        if char in arr[i]:
            res += i + 3

print(res)
