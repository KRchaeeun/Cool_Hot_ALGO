# 농장 관리
def dfs(i, j):
    global is_top

    # 델타 검색(상 하 좌 우 상좌 상우 하좌 하우)
    di = [-1, 1, 0, 0, -1, -1, 1, 1]
    dj = [0, 0, -1, 1, -1, 1, -1, 1]

    visited[i][j] = 1  # 지금 탐색하는 점 방문 표시 1

    for d in range(8):  # 델타 검색 총 8개 방향
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < N and 0 <= nj < M:  # 배열 밖을 벗어 나지 않도록

            if farm[i][j] < farm[ni][nj]:  # 만약 주변이 지금 탐색하는 점보다 큰 점이 있다면
                is_top = False  # 봉우리가 아니므로 False로 저장

            if not visited[ni][nj] and farm[ni][nj] == farm[i][j]:  # 만약 방문한 점이 아니고 같은 높이가 있다면
                dfs(ni, nj)  # 그 점을 그룹화하고 주변을 다시 dfs 탐색 (재귀)


N, M = map(int, input().split())  # 농장의 크기 N X M
farm = [list(map(int, input().split())) for _ in range(N)]  # farm: 농장 정보 입력받기
visited = [[0] * M for _ in range(N)]  # visited: 방문을 표시할 배열
cnt = 0  # cnt: 산봉우리의 개수를 저장할 변수, 초기값 0

for i in range(N):
    for j in range(M):
        if farm[i][j] > 0 and not visited[i][j]:  # 방문한적이 없고 0보다 크다면
            is_top = True  # is_top: 산봉우리인지 아닌지를 초기값 True로 하고
            dfs(i, j)  # dfs함수 호출하여 재귀 시작
            if is_top:  # 만약 dfs 재귀함수 후에도 True로 나온다면
                cnt += 1  # 산봉우리이므로 카운트 1 해준다

print(cnt)  # 출력