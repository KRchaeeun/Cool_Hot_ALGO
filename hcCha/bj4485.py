'''
backtraking, dfs, 백트래킹..?
최소금액.. 가지치기..
backtraking..

#########시간초과#######
import sys
input = sys.stdin.readline


def backtraking(x, y, cost):
    global min_cost

    if x == size - 1 and y == size - 1:
        min_cost = min(min_cost, cost)

    else:
        delta = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for nx, ny in delta:
            if 0 <= nx < size and 0 <= ny < size and visited[nx][ny] == 0:
                if cost + matrix[nx][ny] >= min_cost:
                    continue
                visited[nx][ny] = 1
                backtraking(nx, ny, cost + matrix[nx][ny])
                visited[nx][ny] = 0


tc = 0
while True:
    tc += 1
    size = int(input())
    if size == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(size)]

    min_cost = 1e9

    visited = [[0] * size for _ in range(size)]

    visited[0][0] = 1
    backtraking(0, 0, matrix[0][0])  # x, y, cost
    print(f'Problem {tc}:', min_cost)


##############bfs 풀이##############
from collections import deque


def bfs():
    q = deque([])
    q.append((0, 0))
    # 첫 위치에 금액 설정
    visited[0][0] = matrix[0][0]

    while q:
        x, y = q.popleft()

        # 상하좌우 탐색
        delta = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
        for nx, ny in delta:
            if 0 <= nx < size and 0 <= ny < size:
                # 방문할 지역에 적힌 금액보다 내가 방문했을 때 금액이 적은 경우 진행
                if visited[nx][ny] > visited[x][y] + matrix[nx][ny]:
                    visited[nx][ny] = visited[x][y] + matrix[nx][ny]
                    q.append((nx, ny))


tc = 0
while True:
    tc += 1
    size = int(input())
    if size == 0:
        break

    matrix = [list(map(int, input().split())) for _ in range(size)]

    # ###중요### 방문기록 / 해당 위치에 도달하기 까지 누적금액의 최소를 기록하기 위해 큰 수를 넣어둔다.
    # float("inf") = 양의 무한대
    visited = [[float("inf")] * size for _ in range(size)]

    bfs()  # x, y, cost
    print(f'Problem {tc}:', visited[size - 1][size - 1])
'''


