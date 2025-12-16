while True:
    s = input()
    S = []
    if s == ".":
        break
    for i in s:
        if i == "(":
            S.append("(")
        elif len(S) != 0 and S[-1] == "(" and i == ")":
            S.pop()
        elif i == ")":
            S.append(")")
        if i == "[":
            S.append("[")
        elif len(S) != 0 and S[-1] == "[" and i == "]":
            S.pop()
        elif i == "]":
            S.append("]")
    print("yes" if len(S) == 0 else "no")
