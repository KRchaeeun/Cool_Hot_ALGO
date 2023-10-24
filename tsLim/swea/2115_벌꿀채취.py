# 1번 벌
def f1(n, cnt, sum_profit, i, j):
    global max_profit1
    # 종료 조건
    # 채취할 꿀 크기가 넘었으면
    if cnt > C:
        return
    # 다 채취 했으면
    if n == M:
        max_profit1 = max(max_profit1, sum_profit)
        return

    # 다음 꿀통의 위치, 현재까지 채취한 꿀 크기, 현재까지 이익, 처음 주어진 위치 i, j
    # 꿀통을 선택하는 경우
    f1(n+1, cnt+arr[i][j+n], sum_profit+arr[i][j+n]**2, i, j)
    # 꿀통 선택 안하고 다음 걸로 넘어가는 경우
    f1(n+1, cnt, sum_profit, i, j)

# 2번 벌
def f2(n, cnt, sum_profit, i, j):
    global max_profit2

    if cnt > C:
        return
    if n == M:
        max_profit2 = max(max_profit2, sum_profit)
        return

    f2(n+1, cnt+arr[i][j+n], sum_profit+arr[i][j+n]**2, i, j)
    f2(n+1, cnt, sum_profit, i, j)



T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    res = 0
    # 첫 번째 일꾼
    for i1 in range(N):
        for j1 in range(N-M+1):
            max_profit1 = 0
            f1(0, 0, 0, i1, j1)
            # 두 번째 일꾼
            for i2 in range(i1, N):
                # 같은 줄 에서 구할 경우
                if i1 == i2:
                    sj = j1+M
                # 그 외 경우
                else:
                    sj = 0
                for j2 in range(sj, N-M+1):
                    max_profit2 = 0
                    f2(0, 0, 0, i2, j2)
                    # 결과값 계산
                    res = max(res, max_profit1+max_profit2)

    print(f'#{tc} {res}')