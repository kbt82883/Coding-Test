N, B = input().split()
B = int(B)
arr = list(N)
res = 0

a = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

for i in range(len(arr) - 1, -1, -1):
    try:
        n = a.index(arr[i]) + 10
    except:
        n = int(arr[i])

    res += (B ** (len(arr) - i - 1)) * n

print(res)
