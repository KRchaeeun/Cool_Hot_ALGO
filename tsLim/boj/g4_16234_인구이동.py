from collections import deque

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(i, j):
    q = deque()
    union = []
    q.append((i, j))
    union.append((i, j)) # 연합만들기
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[x][y] - A[nx][ny]) <= R: # 둘의 차가 범위 안일때만 진행
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))
    return union # 연합을 리턴


N, L, R = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

result = 0
while True:
    visited = [[0]*N for _ in range(N)]
    flag = 0 # 아무것도 안할경우 탈출하기 위한 조건
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                nara = bfs(i, j)

                if len(nara) > 1:
                    total = 0
                    for x, y in nara:
                        total += A[x][y] # 연합의 인구 합
                    people = total // len(nara) # 소수점 제외
                    flag = 1 # 된거니까 그대로 진행
                    for x, y in nara:
                        A[x][y] = people # 바꿔주기
    if not flag:
        break
    result += 1 # 이동 기간 하루 더하기
print(result)


