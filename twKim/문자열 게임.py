import sys
input = sys.stdin.readline

N, M = map(int, input().split())
my_sen = input().strip()
sen = input().strip()
max_point = 0

dp = [0] * N
dp1 = [0] * N

for i in range(M):
    dp1 = [0] * N
    for j in range(N):
        if my_sen[j] == sen[i]:
            dp[j] += 1
        
        if dp[j]:
            if j - 1 >= 0:
                dp1[j - 1] = max(dp1[j - 1], dp[j])
            
            if j + 1 < N:
                dp1[j + 1] = max(dp1[j + 1], dp[j])
        
            dp[j] = 0

    for j in range(N):
        dp[j] = dp1[j]

for i in dp1:
    max_point = max(max_point, i)
print(max_point)