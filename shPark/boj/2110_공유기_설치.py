import sys
# input = sys.stdin.readline

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()
start, end = 1, houses[N-1] - houses[0]

res = 0
if C == 2:
    print(end)
else:
    while start <= end:
        mid = (start + end)//2

        cnt = 1
        now = houses[0]
        for i in range(N):
            if houses[i] - now >= mid:
                cnt += 1
                now = houses[i]

        if cnt >= C:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    print(res)
