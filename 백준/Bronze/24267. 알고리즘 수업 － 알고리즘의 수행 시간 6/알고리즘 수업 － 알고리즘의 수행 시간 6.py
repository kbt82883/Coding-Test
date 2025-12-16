n = int(input())
k = 1
cnt = 0
for i in range(2, n):
    cnt += k
    k += i

print(cnt)
print(3)
