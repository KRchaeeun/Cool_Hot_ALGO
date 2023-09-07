import sys
from collections import deque

N = int(input())
graph = [[0] * N for _ in range(N)]

# 사과 위치 저장
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

# 방향 변경 정보 저장
direction = {}
L = int(input())
for _ in range(L):
    x, c = input().split()
    direction[int(x)] = c

# 뱀 처음 위치
snake_pos = deque([[0, 0]])

# 북 동 남 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 뱀 처음 방향: 동
d = 1
times = 0
nx, ny = 0, 0

def change_direction(curr_d, turn):
    if turn == "D":
        curr_d = (curr_d+1) % 4
    else:
        curr_d = (curr_d-1) % 4
    return curr_d

while True:
    times += 1
    nx += di[d]
    ny += dj[d]

    # 벽에 부딪히거나 자신의 몸에 부딪히면 종료
    if not(0 <= nx < N and 0 <= ny < N) or [nx, ny] in snake_pos:
        break

    # 사과가 있다면 먹고, 몸길이 증가
    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        snake_pos.append([nx, ny])
    # 사과가 없다면 몸길이를 줄임 (꼬리 위치를 제거)
    else:
        snake_pos.append([nx, ny])
        snake_pos.popleft()

    # 방향 전환 정보가 있다면 방향 전환
    if times in direction.keys():
        d = change_direction(d, direction[times])

print(times)