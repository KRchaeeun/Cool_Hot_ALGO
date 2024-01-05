from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    matrix[x][y] = 0
    total = 1
    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append((nx, ny))
                total += 1

    return total


N, M, K = map(int, input().split())
matrix = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = 1

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
max_v = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            max_v = max(max_v, bfs(i, j))

print(max_v)