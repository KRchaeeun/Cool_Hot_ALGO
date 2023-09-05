import sys

# input = sys.stdin.readline


# 완전탐색
def dfs(life, cnt, happy):
    if life < 1:
        return

    if cnt == n:
        res.append(happy)
        return

    dfs(life - info[cnt][0], cnt + 1, happy + info[cnt][1])
    dfs(life, cnt + 1, happy)


n = int(input())

cost_reward = list(map(int, input().split()))
cost_reward.extend(list(map(int, input().split())))
info = []
for i in range(n):
    info.append([cost_reward[i], cost_reward[i + n]])

# 그리디로 접근하기 위해 행복 순으로 정렬
info.sort(key=lambda x: -x[1])

res = []

dfs(100, 0, 0)

print(max(res))
