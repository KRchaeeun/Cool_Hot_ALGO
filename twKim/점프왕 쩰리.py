import sys
input = sys.stdin.readline

def dfs(x,y):
    global T_F

    if T_F:
        return
    
    if x == N - 1 and y == N - 1:
        T_F = 1
        return


    for k in range (2):

        nx = x + delta[k][0] * matrix[x][y]
        ny = y + delta[k][1] * matrix[x][y]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny)
            visited[nx][ny] = 0


N = int(input())
delta = ((1,0), (0,1))
matrix = [list(map(int, input().split())) for _ in range (N)]
visited = [[0]*N for _ in range (N)]
T_F = 0
visited[0][0] = 1
dfs(0,0)

if T_F:
    print('HaruHaru')
else :
    print('Hing')