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
                q.append((nx, ny, idx))

    return cnt


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

print(bfs(0, 1, 0))


def dfs(x, y, direc):
    global cnt
    if cnt >= 1000000:
        return
    if x == size - 1 and y == size - 1:
        cnt += 1

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