lst = list(map(int, input().split()))

lst.sort()

a, b, c = lst[0], lst[1], lst[2]

while c >= a + b:
    c -= 1

print(a + b + c)
