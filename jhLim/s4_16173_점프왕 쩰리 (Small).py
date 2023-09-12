import sys
input = sys.stdin.readline

def dfs(area):
    visited = [[0] * N for _ in range(N)]
    stack = [(0, 0)]
    dx = [0, 1]
    dy = [1, 0]
    sx, sy = 0, 0
    stack.append((sx, sy))

    while stack:
        if area[sx][sy] == -1:
            return 'HaruHaru'

        for i in range(2):
            nx = sx + dx[i] * area[sx][sy]
            ny = sy + dy[i] * area[sx][sy]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))
                sx, sy = nx, ny
                break
        else:
            if stack:
                sx, sy = stack.pop()
    return 'Hing'

N = int(input().rstrip())
area = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(dfs(area))