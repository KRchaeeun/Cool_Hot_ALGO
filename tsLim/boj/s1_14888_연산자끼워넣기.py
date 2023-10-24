import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 14888
N = int(input())
num = list(map(int, input().split()))
plus, minus, multiply, division = map(int, input().split())
max_cnt = -1e9
min_cnt = 1e9


def f(i, res): # i : 현재까지 계산한 숫자의 수, res : 현재까지 계산한 값
    global plus, minus, multiply, division, max_cnt, min_cnt
    if i == N: # 전부 다 계산했으면 결과 찾기
        max_cnt = max(max_cnt, res)
        min_cnt = min(min_cnt, res)

    # 더하기
    if plus > 0:
        plus -= 1
        f(i+1, res+num[i])
        plus += 1
    # 빼기
    if minus > 0:
        minus -= 1
        f(i+1, res-num[i])
        minus += 1
    # 곱하기
    if multiply > 0:
        multiply -= 1
        f(i+1, res*num[i])
        multiply += 1
    # 나누기
    if division > 0:
        division -= 1
        # 양수일때
        if res >= 0:
            f(i+1, res//num[i])
        # 음수일때
        if res < 0:
            f(i+1, -(abs(res) // num[i]))
        division += 1


f(1, num[0])
print(int(max_cnt))
print(int(min_cnt))