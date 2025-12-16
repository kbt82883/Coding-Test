for _ in range(int(input())):
    S = []
    lst = list(input().strip())
    for s in lst:
        if s == "(":
            S.append("(")
        elif len(S) != 0 and S[-1] == "(" and s == ")":
            S.pop()
        else:
            S.append(")")
    print("YES" if len(S) == 0 else "NO")
