# bfs 탐색 함수 설정
def bfs(x,y,N,game):
    q = []
    q.append((x,y))
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = '?'
    while q:
        # result를 리턴할것이기 때문에 일단 인덱스를 벗어나는 경우에 출력해야 하는 Hing으로 설정
        result = 'Hing'
        # 초기 큐 팝
        x,y = q.pop(0)
        pump = game[x][y]
        # 좌표값이 -1 이면 완료 처리
        if game[x][y]==-1:
            result = 'HaruHaru'
            return result
        # 우, 하 탐색 델타 설정
        for dx,dy in [[0,1],[1,0]]:
            nx,ny = x+dx*pump,y+dy*pump
            # 인덱스 유효하고 visited가 ?값을 가지지 않는 경우 큐에 추가
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] != '?':
                q.append((nx,ny))
                # 이후 visited에 ? 설정
                visited[nx][ny] = '?'
    return result

N = int(input())
game = [list(map(int,input().split())) for _ in range(N)]
# 함수 실행
a = bfs(0,0,N,game)
print(a)
