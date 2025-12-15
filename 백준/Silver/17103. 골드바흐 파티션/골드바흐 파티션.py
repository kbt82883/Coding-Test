import sys

input = sys.stdin.readline


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


lst = sieve(1000000)
for _ in range(int(input())):
    N = int(input())

    cnt = 0
    for i in range(2, N // 2 + 1):
        if lst[i] and lst[N - i]:
            cnt += 1

    print(cnt)
