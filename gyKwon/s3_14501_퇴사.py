import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(1, N + 1):
    day, pay = map(int, input().split())
    day -= 1

    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    if i + day <= N:
        if dp[i + day] < dp[i-1] + pay:
            dp[i + day] = dp[i-1] + pay

print(dp[N])