N = int(input())  # 사람의 수
loss_health = list(map(int, input().split()))  # 잃는 체력 입력값
gain_happy = list(map(int, input().split()))  # 얻는 기쁨 입력값
dp =[[0]*101 for _ in range(N+1)]  # dp 초기상태 (0~100까지 총 101개)
for i in range(1, N+1):
    for j in range(1, 101):
        # 만약 j가 i-1번째 사람의 잃는 체력보다 크거나 같다면
        # 그 위에 저장되어있는 값과 i-1번째 사람의 기쁨을 더한 것중에 큰 것을 저장
        if loss_health[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss_health[i-1]] + gain_happy[i-1])

        else:  # 아니라면 전행에 있는 dp로 저장
            dp[i][j] = dp[i-1][j]
print(dp[N][99])  # 출력