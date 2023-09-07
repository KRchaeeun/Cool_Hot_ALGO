import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
matrix = [[0] * N for _ in range(N)]
delta = ((0, 1), (1, 0), (0, -1), (-1, 0))

apple_cnt = int(input())                        # 보드판에 사과 배치
for _ in range(apple_cnt):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1

change_dr_cnt = int(input())                    # 방향을 바꾸는 횟수
change_dr_list = deque([])                      # 방향 정보를 입력받는 리스트 [0번이 시간][1번이 방향]
for _ in range(change_dr_cnt):
    a, b = map(str, input().split())
    a = int(a)
    change_dr_list.append((a, b))

dr = 0                                          # 첫 방향은 오른쪽
stack = [(0, 0)]                                # 시작점
time = 0                                        # 시간
ch_time, ch_dr = change_dr_list.popleft()       # 방향 정보를 저장해둠
line = deque([(0, 0)])                          # 뱀의 길이
while stack:

    x, y = stack.pop()                          # dfs시작
    if time == ch_time:                         # 지금 시간이 방향이 바뀌는 시간인지 확인
        if ch_dr == 'D':                        # D면 오른쪽으로 90도 꺽어줌
            dr = (dr + 1) % 4
        else:                                   # 아니면 왼쪽으로 90도 꺽어줌
            dr = (dr + 3) % 4
        if change_dr_list:
            ch_time, ch_dr = change_dr_list.popleft() # 방향 바꿧으면 다음 방향 바꾸는 정보를 받아옴

    nx = x + delta[dr][0]
    ny = y + delta[dr][1]
    time += 1
    if 0 <= nx < N and 0 <= ny < N:             # 범위 정보
        if (nx, ny) in line:                    # 뱀 몸에 닿는지 확인
            break
        if matrix[nx][ny] == 1:                 # 사과를 먹는지 확인
            line.append((nx, ny))
            matrix[nx][ny] = 0
        else:
            line.append((nx, ny))
            line.popleft()
        stack.append((nx, ny))
    else:
        break

print(time)                                     # 시간 출력