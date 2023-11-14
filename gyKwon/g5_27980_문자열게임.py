################# 미완성 된 코드


n, m = map(int, input().split())
board = input()
word = input()

dp = [[0] * (m + 1) for _ in range(n + 1)]

max_score = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if board[i - 1] == word[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_score = max(max_score, dp[i][j])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


print(max_score)
