# BOJ_16173 : 점프왕 쩰리(Small)
import sys

# input = sys.stdin.readline
sys.stdin = open('input.txt')

# 재귀 깊이 늘리기 사실 필요 없음
sys.setrecursionlimit(10**6)


# dfs 로 탐색
def ck_avail(x, y):
    global flg

    # 거리 측정
    dis = fld[x][y]
    # 맨끝에 도달하면 조건에따라 무조건 끝
    if x == size - 1 and y == size - 1:
        flg = True
        return

    # 0이면 못가니까
    if dis == 0:
        return

    # 0이 아니면 진행
    for di, dj in [[0, 1], [1, 0]]:
        ni, nj = di * dis + x, dj * dis + y
        if 0 <= ni < size and 0 <= nj < size:
            ck_avail(ni, nj)


size = int(input())
fld = [list(map(int, input().rstrip().split())) for _ in range(size)]
# visited 따윈 필요없다
flg = False
ck_avail(0, 0)
if flg:
    print('HaruHaru')
else:
    print('Hing')
