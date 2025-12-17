import sys

input = sys.stdin.readline


def is_palindrome(s1, l, r, memo):
    if l >= r:
        return 1
    elif s1[l] != s1[r]:
        return 0
    else:
        memo[0] += 1
        return is_palindrome(s1, l + 1, r - 1, memo)


for _ in range(int(input())):
    s1 = input().strip()
    memo = [1]
    res = is_palindrome(s1, 0, len(s1) - 1, memo)
    print(res, memo[0])
