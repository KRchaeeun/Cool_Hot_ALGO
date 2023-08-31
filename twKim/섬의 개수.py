import sys
input = sys.stdin.readline

def dfs(i,j):

    stack = [(i,j)]

    while stack:

        x,y = stack.pop()

        for k in range (8):

            nx = x + delta[k][0]
            ny = y + delta[k][1]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] == 1 :
                visited[nx][ny] = 1
                stack.append((nx,ny))
        

while True:

    M, N = map(int, input().split())
    if not N and not M:
        break

    matrix = [list(map(int, input().split())) for _ in range (N)]
    visited = [[0]*M for _ in range (N)]
    delta = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1),(-1,-1))
    cnt = 0
    
    for i in range (N):
        for j in range (M):
            if matrix[i][j] == 1 and not visited[i][j]:       # 그래프 탐색
                cnt += 1
                visited[i][j] = 1
                dfs(i,j)                                        # bfs든 dfs든 둘다 상관없음
    print(cnt)                                                  # 뭉쳐있으면 센다