a = int(input())
b = int(input())

result = 0

for i in range(3):
    print(a * (b % 10))
    result += a * (b % 10) * 10**i
    b //= 10
print(result)
