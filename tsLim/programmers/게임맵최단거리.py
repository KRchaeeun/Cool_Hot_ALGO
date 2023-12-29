from collections import deque
delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    if maps[N-1][M-1] == 1:
        answer = -1
    else:
        answer = maps[N-1][M-1]
    return answer