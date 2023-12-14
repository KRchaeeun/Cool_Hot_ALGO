import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, value):
    global Border
    global flag

    q = deque()
    q.append((a, b))
    count = 1
    temp = [(a, b)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if L <= abs(matrix[x][y] - matrix[nx][ny]) <= R:
                    flag = 1
                    visited[nx][ny] = Border
                    count += 1
                    value += matrix[nx][ny]
                    q.append((nx, ny))
                    temp.append((nx, ny))
    
    return temp, count, value


N, L, R = map(int, input().strip().split())

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
matrix = [list(map(int, input().strip().split())) for i in range(N)]
visited = list([-1] * N for i in range(N))
flag = 1
print_num = 0

while flag :
    visited = list([-1] * N for i in range(N))
    flag = 0
    Border = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                Border += 1
                visited[i][j] = Border
                temp, count, value = bfs(i, j, matrix[i][j])
                for x, y in temp:
                    matrix[x][y] = value // count
    if flag == 0:
        break
    print_num += 1
    print(matrix)

# print(matrix)
print(print_num)