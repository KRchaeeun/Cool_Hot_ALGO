# bfs 함수 설정
def bfs(x,y):
    # 큐 설정
    q = []
    q.append((x,y))
    # 양을 찾으면 '.'
    grass[x][y] = '.'
    while q:
        x,y = q.pop(0)
        # 델타 탐색으로 양 찾기
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
            nx,ny = x+dx,y+dy
            # 이동했을시 좌표가 유효한 인덱스인 경우
            if 0<=nx<H and 0<=ny<W:
                # '#'를 찾으면 좌표를 큐에 푸시
                if grass[nx][ny]=='#':
                    q.append((nx,ny))
                    grass[nx][ny] = '.'
                    # 찾았으니 재방문을 막기 위해 '.' 표시

# 양 발견시 탐색을 시작하는 함수 설정
def wheres(W,H):
    global cnt
    for i in range(H):
        for j in range(W):
            if grass[i][j] == '#':
                bfs(i,j)
                # 함수가 한 번 진행된다면 무리 하나를 발견한것이므로 카운트 +1
                cnt+=1


T = int(input())
for tc in range(T):
    H,W = map(int,input().split())
    # 양과 풀의 위치를 2차원 배열로 받기
    grass = [list(input()) for _ in range(H)]
    # 무리의 수를 세주는 카운트 변수 설정
    cnt = 0
    wheres(W, H)
    print(cnt)