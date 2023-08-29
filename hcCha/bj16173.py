def dfs(x, y):
    global rst
    # 종료 조건 -1 인경우 결과값 변경하고 리턴
    if matrix[x][y] == -1:
        rst = 1
        return
    # 큐가 빌 때까지 / 모든 탐색 마칠 때 까지
    while que:
        # 기준점 설정
        (nx, ny) = que.pop(0)
        # 이동가능지역 탐색
        for k in range(2):
            # 기준점 위치에 해당하는 값 만큼 이동거리 추가
            g = matrix[nx][ny]
            ni = nx + di[k] * g
            nj = ny + dj[k] * g
            # 이동할 지역이 범위 내 and 방문 안했다면
            if 0 <= ni < size and 0 <= nj < size:
                if visited[ni][nj] == 0:
                    # 방문하기 위해 큐에 추가 + 해당지역 방문 설정 후 함수 호출
                    que.append((ni, nj))
                    visited[ni][nj] = 1
                    dfs(ni, nj)


size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
rst = 0

# 아래, 오른쪽만 가능 / 경우의수 2가지
di = [0, 1]
dj = [1, 0]

# 방문기록
visited = [[0] * size for _ in range(size)]

# 큐에 추가
que = [(0, 0)]
dfs(0, 0)
if rst == 1:
    print('HaruHaru')
else:
    print('Hing')