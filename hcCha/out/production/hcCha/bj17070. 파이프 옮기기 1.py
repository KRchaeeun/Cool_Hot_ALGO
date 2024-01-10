from collections import deque
import sys
input = sys.stdin.readline
'''
##########################시간 초과##############################
def bfs(x, y, cnt):
    # 위치, 방향 / 1인 경우 가로, 2인 경우 세로, 3인 경우 대각선
    q = deque([(x, y, 1)])

    while q:
        # x, y, 현재 방향
        x, y, direction = q.popleft()
        delta = [(x, y + 1), (x + 1, y), (x + 1, y + 1)]
        # 목표지점 도착시 + 1
        if x == size - 1 and y == size - 1:
            cnt += 1
        if cnt == 1000000:
            return cnt

        # 탐색 방향 표시
        idx = 0

        for nx, ny in delta:
            idx += 1
            # 현재 방향에 따라 불가능 탐색방향인 경우 패스
            if (direction == 1 and idx == 2) or (direction == 2 and idx == 1):
                continue
            # 범위 내 이면서 빈 곳인 경우
            if 0 <= nx < size and 0 <= ny < size and matrix[nx][ny] == 0:
                # 대각선 탐색 중인 경우 주변 3칸 중 벽이 있다면 패스
                if idx == 3 and (matrix[nx - 1][ny] == 1 or matrix[nx][ny - 1] == 1):
                    continue
                if dp[nx][ny][idx] == 1:
                    continue
                q.append((nx, ny, idx))

    return cnt


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
dp = [[[0] * 4 for _ in range(size)] for _ in range(size)]

print(bfs(0, 1, 0))

###################성공과 실패#################
def dfs(x, y, direc):
    global cnt
    if cnt >= 1000000:
        return

    if x == size - 1 and y == size - 1:
        cnt += 1
        return

    # 대각선인 경우
    if x + 1 < size and y + 1 < size:
        if matrix[x + 1][y + 1] == 0 and matrix[x + 1][y] == 0 and matrix[x][y + 1] == 0:
            dfs(x + 1, y + 1, 3)

    # 세로인 경우
    if x + 1 < size and (direc == 2 or direc == 3):
        if matrix[x + 1][y] == 0:
            dfs(x + 1, y, 2)

    # 가로인 경우
    if y + 1 < size and (direc == 1 or direc == 3):
        if matrix[x][y + 1] == 0:
            dfs(x, y + 1, 1)

########################################################################################

    ### 델타와 for문으로 시간초과 ###
    delta = [(x, y + 1), (x + 1, y), (x + 1, y + 1)]
    # 탐색 방향 표시
    idx = 0
    for nx, ny in delta:
        idx += 1
        # 현재 방향에 따라 불가능 탐색방향인 경우 패스
        if (direc == 1 and idx == 2) or (direc == 2 and idx == 1):
            continue
        # 범위 내 이면서 빈 곳인 경우
        if 0 <= nx < size and 0 <= ny < size and matrix[nx][ny] != 1:
            # 대각선 탐색 중인 경우 주변 3칸 중 벽이 있다면 패스
            if idx == 3 and (matrix[nx - 1][ny] == 1 or matrix[nx][ny - 1] == 1):
                continue
            dfs(nx, ny, idx)


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

cnt = 0
dfs(0, 1, 1)
print(cnt)
'''
# DP는 신이고 무적이다.
size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
dp = [[[0] * 3 for _ in range(size)] for _ in range(size)] # 0대각선 1 가로 2세로
# 출발 세팅
dp[0][1][1] = 1
# 첫 줄, 0행은 출발지의 가로 상태에서만 이동 가능하니 기록
for i in range(2, size):
    if matrix[0][i] == 0:
        dp[0][i][1] = dp[0][i - 1][1]

for i in range(1, size):
    for j in range(1, size):
        # 이동이 가능한 경우
        if matrix[i][j] == 0:
            # ij의 대각선이 가능한 경우
            if matrix[i][j - 1] == 0 and matrix[i - 1][j] == 0:
                # 꼬리부분 도착 가능 경우 합
                dp[i][j][0] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][2] + dp[i - 1][j - 1][1]

            # 가로 이동이 가능한 경우
            # 꼬리 부분에서 가로로 이동 가능한 경우 합
            dp[i][j][1] = dp[i][j - 1][0] + dp[i][j - 1][1]
            # 세로 이동이 가능한 경우
            # 꼬리 부분에서 세로로 이동 가능한 경우 합
            dp[i][j][2] = dp[i - 1][j][0] + dp[i - 1][j][2]

# 최종적으로 도착지의 모든 경우의수 합
print(dp[size - 1][size - 1][0] + dp[size - 1][size - 1][1] + dp[size - 1][size - 1][2])

