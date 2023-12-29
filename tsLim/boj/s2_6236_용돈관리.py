N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]

start = min(arr)
end = sum(arr)
res = 0

while start <= end:
    mid = (start + end) // 2
    money = mid
    cnt = 1
    for i in arr:
        if money < i:
            money = mid
            cnt += 1
        money -= i

    if cnt > M or mid < max(arr):
        start = mid + 1
    else:
        end = mid - 1
        res = mid

print(res)