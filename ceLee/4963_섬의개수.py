from collections import deque
# 델타 검색: 상 하 좌 우
di = [-1, 1, 0, 0, -1, -1, 1, 1]
dj = [0, 0, -1, 1, -1, 1, -1, 1]

def BFS(i, j):
    stack = deque([])
    stack.append([i, j])
    while stack:
        x, y = stack.popleft()
        for d in range(8):
            nx = x + di[d]
            ny = y + dj[d]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny]:
                field[nx][ny] = 0
                stack.append([nx, ny])

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    field = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0

    for i in range(h):
        for j in range(w):
            if field[i][j]:
                field[i][j] = 0
                BFS(i, j)
                cnt += 1
    print(cnt)