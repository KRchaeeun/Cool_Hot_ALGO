import sys
input = sys.stdin.readline


N = int(input())
dp = [0]*100
help_list = list(map(int, input().split()))
happy_list = list(map(int, input().split()))
for i in range(N):
    v, w = help_list[i], happy_list[i]
    for j in range(99, v-1, -1):
        dp[j] = max(dp[j], dp[j - v] + w)
print(max(dp))