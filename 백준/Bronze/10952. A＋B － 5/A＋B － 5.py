flag = True
while flag:
    A,B = map(int,input().split())
    res = A+B
    if res == 0:
        flag = False
        break
    print(res)