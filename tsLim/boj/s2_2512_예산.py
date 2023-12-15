# N : 지방의 수, arr : 각 지방의 예산 요청을 표현하는 N개의 정수, M : 총 예산
N = int(input())
arr = list(map(int, input().split()))
M = int(input())

# 이분탐색
start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
