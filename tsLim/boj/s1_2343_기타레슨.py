N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
start, end = max(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2
    count = 0
    sum = 0
    for i in range(N):
        if sum + arr[i] > mid:
            count += 1
            sum = 0
        sum += arr[i]

    if sum:
        count += 1

    if count <= M:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)
