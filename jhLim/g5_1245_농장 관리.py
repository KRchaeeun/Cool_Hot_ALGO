import sys, copy
input = sys.stdin.readline

def dfs(x, y):
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    stack = [(x, y)]

    while stack:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                if arr[x][y] < arr[nx][ny]:
                    return 0
                elif arr[x][y] == arr[nx][ny]:
                    visited[nx][ny] = 1
                    stack.append((x, y))
                    x = nx
                    y = ny
                    break
                else:
                    visited[nx][ny] = 1
        else:
            x, y = stack.pop()

    return 1


def m(x, y):
    visited = [[0]*M for _ in range(N)]
    visited[x][y] = 1
    marr[x][y] = 1
    stack = [(x, y)]

    while stack:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                if arr[x][y] == arr[nx][ny]:
                    visited[nx][ny] = 1
                    marr[nx][ny] = 1
                    stack.append((x, y))
                    x = nx
                    y = ny
                    break
        else:
            x, y = stack.pop()


N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
marr = [[0]*M for _ in range(N)]
cnt = 0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(N):
    for y in range(M):
        if arr[x][y] != 0 and marr[x][y] == 0:
            if dfs(x, y) == 1:
                cnt += dfs(x, y)
                m(x, y)

print(cnt)