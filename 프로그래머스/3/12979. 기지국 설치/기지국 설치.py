def solution(n, stations, w):
    answer = 0
    cover = 2 * w + 1

    start = 1

    for station in stations:
        left = station - w
        right = station + w

        # 현재 기지국 왼쪽의 빈 구간
        empty = left - start

        if empty > 0:
            answer += (empty + cover - 1) // cover

        # 다음 확인 시작 위치
        start = right + 1

    # 마지막 기지국 이후 빈 구간
    if start <= n:
        empty = n - start + 1
        answer += (empty + cover - 1) // cover

    return answer