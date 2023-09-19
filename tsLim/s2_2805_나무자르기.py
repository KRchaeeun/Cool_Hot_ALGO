# 2805
N, M = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)
res = 0
while start <= end:
    # 이분탐색을 위한 중간값
    mid = (start+end) // 2
    cnt = 0
    # 나무들에 대하여
    for a in arr:
        # 나무가 중간값보다 크면
        if a > mid:
            # 잘라서 저장
            cnt += (a-mid)
        # 이미 다 잘랐으면
        if cnt >= M:
            break

    # 자른 나무가 작다면 끝점을 아래로
    if cnt < M:
        end = mid - 1
    # 크거나 같으면 시작점을 위로
    else:
        # 결과값은 mid값
        res = mid
        start = mid + 1
print(res)