h, m = map(int, input().split())
k = int(input())

m += k
while m >= 60:
    h += 1
    m -= 60
    if h >= 24:
        h -= 24

print(h, m)
