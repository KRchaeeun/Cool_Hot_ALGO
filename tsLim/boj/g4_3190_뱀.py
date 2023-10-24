import sys
input = sys.stdin.readline
from collections import deque

# 3190
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def f(j, i):
    if i == 'D':
        j = (j + 1) % 4
    else:
        j = (j - 1) % 4
    return j


def snake():
    direction = 1
    time = 1
    x, y = 0, 0
    # 뱀이 지나간 위치 덱에 저장
    visited = deque([[x, y]])
    # 지금 뱀이 있는 위치를 2로 바꾸어 둠
    arr[x][y] = 2
    while True:
        x, y = x+dx[direction], y+dy[direction]
        # 범위를 벗어나지 않고 뱀이 자기 자신을 만나지 않았을 때
        if 0<=x<N and 0<=y<N and arr[x][y] != 2:
            # 사과를 만나지 못했을 때
            if arr[x][y] != 1:
                nx, ny = visited.popleft()
                arr[nx][ny] = 0
            # 아닌 경우는 그냥 자기 자신을 표시
            arr[x][y] = 2
            visited.append([x, y])
            # 돌아야 하는 시점일 경우
            if time in t.keys():
                direction = f(direction, t[time])
            time += 1
        else:
            return time


N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
L = int(input())
t = {}
for i in range(L):
    X, C = input().split()
    t[int(X)] = C

print(snake())