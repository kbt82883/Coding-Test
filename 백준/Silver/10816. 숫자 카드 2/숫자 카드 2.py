N = int(input())
dic = {}
lst = list(map(int, input().split()))
for n in lst:
    dic[n] = dic.get(n, 0) + 1

M = int(input())
lst2 = list(map(int, input().split()))
for n in lst2:
    print(dic.get(n, 0), end=" ")
