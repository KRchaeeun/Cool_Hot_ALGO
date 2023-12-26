import sys
input = sys.stdin.readline
import heapq

def BFS(x, y):

    q = []
    heapq.heappush(q, (0, x, y))

    while q:
        dist, x, y = heapq.heappop(q)

        if dist > visited[x][y]:
            continue
        
        for i in range(4):

            nx = x + delta[i][0]
            ny = y + delta[i][1]

            if 0 <= nx < N and 0 <= ny < M :
                n_dist = visited[x][y] + matrix[nx][ny]
                if n_dist < visited[nx][ny]:
                    visited[nx][ny] = n_dist
                    heapq.heappush(q, (n_dist, nx, ny))


M, N = map(int, input().strip().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))
visited = [[float('INF')] * M for _ in range(N)]
visited[0][0] = 0
BFS(0, 0)
# print(matrix)
print(visited[N-1][M-1])