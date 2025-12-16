a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    res = 10000 + (a * 1000)
elif a == b or b == c or c == a:
    if a==b or a==c:
        res = 1000 + (a * 100)
    else:
        res = 1000 + (b * 100)
else:
    arr = [a, b, c]
    res = sorted(arr)[2] * 100

print(res)
