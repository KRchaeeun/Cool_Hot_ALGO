import sys

N = int(sys.stdin.readline())
dehealth = list(map(int,sys.stdin.readline().split()))
inhealth = list(map(int,sys.stdin.readline().split()))

maxa = 0
# 비트 연산자를 활용하여 부분집합을 구한다
for i in range(1<<N):
    sjhealth = 100
    joy = 0
    for j in range(N):
        # 체력이 0이 되지 않는 경우의 최대 행복 값을 구하기
        if i&(1<<j):
            sjhealth -= dehealth[j]
            joy += inhealth[j]
    if sjhealth > 0:
        maxa = max(maxa,joy)

print(maxa)