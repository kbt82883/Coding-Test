while True:

    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    lst.sort()
    a, b, c = lst[0], lst[1], lst[2]

    if c < a + b:
        if a == b and b == c and c == a:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        elif a != b and b != c and a != c:
            print("Scalene")
    else:
        print("Invalid")
