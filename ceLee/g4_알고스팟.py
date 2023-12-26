import heapq
import sys
sys.stdin = open("input.txt")
# input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited = [[0]*n for _ in range(m)]

    queue = []
    heapq.heappush(queue, (0, x, y))
    visited[x][y] = 1

    while queue:
        count, now_x, now_y = heapq.heappop(queue)

        if now_x == m-1 and now_y == n-1:
            return count
        
        for d in range(4):
            next_x, next_y = now_x + dx[d], now_y + dy[d]
            if 0 <= next_x < m and 0 <= next_y < n and not visited[next_x][next_y]:
                visited[next_x][next_y] = 1

                if graph[next_x][next_y] == 1:
                    heapq.heappush(queue, (count+1, next_x, next_y))

                else:
                    heapq.heappush(queue, (count, next_x, next_y))

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(m)]
print(bfs(0,0))