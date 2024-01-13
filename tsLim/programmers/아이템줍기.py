from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    arr = [[-1] * 102 for _ in range(102)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    arr[i][j] = 0
                elif arr[i][j] != 0:
                    arr[i][j] = 1
    delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    q = deque()
    q.append((characterX * 2, characterY * 2))
    visited = [[1] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = 0

    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if arr[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return answer