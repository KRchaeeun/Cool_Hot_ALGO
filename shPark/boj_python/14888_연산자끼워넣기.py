import sys

# input = sys.stdin.readline


def dfs(plus, minus, times, div, val, cnt):
    if sum([plus, minus, times, div]) == 0:
        res.append(val)
        return

    if plus:
        dfs(plus - 1, minus, times, div, val + nums[cnt], cnt + 1)
    if minus:
        dfs(plus, minus - 1, times, div, val - nums[cnt], cnt + 1)
    if times:
        dfs(plus, minus, times - 1, div, val * nums[cnt], cnt + 1)
    if div:
        if val >= 0:
            dfs(plus, minus, times, div - 1, val//nums[cnt], cnt + 1)
        if val < 0:
            val = abs(val) // nums[cnt]
            dfs(plus, minus, times, div - 1, -val, cnt + 1)


n = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))
res = []
dfs(operations[0], operations[1], operations[2], operations[3], nums[0], 1)
print(max(res))
print(min(res))
