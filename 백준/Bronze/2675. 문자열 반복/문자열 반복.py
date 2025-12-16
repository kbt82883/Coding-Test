T = int(input())

for i in range(T):
    R, S = input().split()

    for i in range(T):
        result = ""
        for j in list(S):
            for k in range(int(R)):
                result += j
    print(result)
