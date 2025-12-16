import sys

# 입력 받기
input = sys.stdin.readline
output = sys.stdout.write

arr = []
N = int(input().rstrip())
for i in range(N):
    arr.append(int(input().rstrip()))

for i in sorted(arr):
    output(str(i) + "\n")
