def bfs(i,j):
    global cnt
    global visited
    # 플래그 설정
    result = 1
    q = []
    q.append((i,j))
    while q:
        # 초기 값 큐에서 팝
        i,j = q.pop(0)
        visited[i][j] = 1
        # 8방향 델타 탐색
        for di,dj in [[1,0],[-1,0],[0,-1],[0,1],[-1,-1,],[1,1],[1,-1],[-1,1]]:
            ni,nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M:
                # 산봉우리가 아니면 플래그 0
                if arr[i][j] < arr[ni][nj]:
                    result=0
                    # 방문하지 않고 최대값과 같다면 -> 산봉우리 조건 부합 -> 큐에 어펜드
                if not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
                    q.append((ni, nj))

    return result

def wheres(N,M):
    # 봉우리 탐색 횟수를 나타내줄 변수 설정
    global cnt
    global visited
    # 해당 좌표값이 0보다 크고 방문하지 않았다면 탐색
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0:
                cnt += bfs(i,j)

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
cnt = 0
visited = [[0] * M for _ in range(N)]
wheres(N,M)
print(cnt)