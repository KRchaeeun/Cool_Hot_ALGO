N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

answer = 0
start, end = max(money), sum(money)
while start <= end:
    mid = (start + end) // 2
    my_money = mid

    day = 1
    for i in money:
        if my_money < i:
            my_money = mid
            day += 1
        my_money -= i

    if day > M:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)