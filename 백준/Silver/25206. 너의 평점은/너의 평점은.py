sum = 0.0
kk = 0.0  # 학점총합
for _ in range(20):
    arr = list(input().split())

    if arr[2] == "P":
        continue

    k = float(arr[1])
    kk += k
    sc = arr[2]
    if sc == "A+":
        sum += 4.5 * k
    elif sc == "A0":
        sum += 4.0 * k
    elif sc == "B+":
        sum += 3.5 * k
    elif sc == "B0":
        sum += 3.0 * k
    elif sc == "C+":
        sum += 2.5 * k
    elif sc == "C0":
        sum += 2.0 * k
    elif sc == "D+":
        sum += 1.5 * k
    elif sc == "D0":
        sum += 1.0 * k
    elif sc == "F":
        sum += 0.0

print(sum / kk)
