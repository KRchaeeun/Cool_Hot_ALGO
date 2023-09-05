import sys
from itertools import permutations
from itertools import combinations

# input = sys.stdin.readline


# 완전탐색
def dfs(life, cnt, happy):
    # 0이되거나 음수가 되면 값을 버려
    if life < 1:
        return

    # 끝까지 탐색을 다 했을때
    if cnt == n:
        res.append(happy)
        return

    dfs(life - info[cnt][0], cnt + 1, happy + info[cnt][1])
    dfs(life, cnt + 1, happy)


n = int(input())
"""
8
100 15 1 2 3 4 6 5
49 40 1 2 3 4 5 4
"""
cost_reward = list(map(int, input().split()))
cost_reward.extend(list(map(int, input().split())))
info = []
for i in range(n):
    info.append([cost_reward[i], cost_reward[i + n]])

print(info)

# 그리디로 접근하기 위해 기쁨 순으로 정렬
info.sort(key=lambda x: -x[1])

print(info)

res = []

dfs(100, 0, 0)

print(res)

print(max(res))
