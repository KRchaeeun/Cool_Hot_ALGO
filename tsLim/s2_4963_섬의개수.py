import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    # 방문확인 남기고 델타탐색
    visited[x][y] = 1
    if arr[x][y] == 1:
        for di, dj in [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
            nx, ny = x+di, y+dj
            # 범위는 넘어가지 않고 땅인 곳을 찾고 방문하지 않은곳을 찾아서
            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    # 0 0이면 종료
    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*(w+1) for _ in range(h+1)]
    cnt = 0
    # 찾아서 함수 호출 시작하고 다 끝나면 카운트
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
            else:
                continue
    print(cnt)