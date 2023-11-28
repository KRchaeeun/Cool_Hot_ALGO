import sys
input = sys.stdin.readline


def dfs(x, y, count):
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for i in range(4):

            nx = x + delta[i][0]
            ny = y + delta[i][1]

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                count += 1
                stack.append((nx, ny))
    
    return count


delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
N, M, K = map(int, input().split())
matrix = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_size = 0
for i in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    matrix[x][y] = 1

for i in range(N):
    for j in range(M):
        if matrix[i][j] and not visited[i][j]:
            visited[i][j] = 1
            max_size = max(dfs(i, j, 1), max_size)

print(max_size)