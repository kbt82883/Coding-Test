import sys

input = sys.stdin.readline


def bt(row):
    global cnt
    global diag1
    global diag2
    global cols

    if row == N:
        cnt += 1
        return
    for col in range(N):
        if cols[col] and diag1[row + col] and diag2[row - col + N - 1]:
            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + N - 1] = False

            bt(row + 1)

            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + N - 1] = True


N = int(input())
cnt = 0
cols = [True] * N
diag1 = [True] * (N * 2)
diag2 = [True] * (N * 2)
bt(0)
print(cnt)
