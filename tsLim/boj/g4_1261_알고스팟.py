from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def bfs(i, j):
    q = deque()
    q.append((0, i, j))
    distance[i][j] = 0
    while q:
        cost, x, y = q.popleft()
        # 시간을 줄이기 위해 추가(없어도 정답)
        if distance[x][y] < cost:
            continue
        # 탐색
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0<=nx<M and 0<=ny<N:
                # 1일경우 벽 부수고
                if maze[nx][ny] == 1:
                    new_cost = cost + 1
                # 아닐경우 기존 값
                else:
                    new_cost = cost
                # 새로운 값이 기존값보다 크거나 같을 경우
                if distance[nx][ny] <= new_cost:
                    continue
                distance[nx][ny] = new_cost
                q.append((new_cost, nx, ny))


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(M)]

# 최소거리 저장 리스트
distance = [[1e9]*N for _ in range(M)]

# 시작점 출발
bfs(0, 0)

print(distance[M-1][N-1])