import sys

# 입력 받기
input = sys.stdin.readline
output = sys.stdout.write

# 첫 줄: 테스트케이스 개수 T
T = int(input().rstrip())

# 결과 저장
results = []

for _ in range(T):
    # 두 정수 A와 B 입력받아 처리
    A, B = map(int, input().rstrip().split())
    results.append(A + B)

# 한 번에 출력
output("\n".join(map(str, results)) + "\n")
