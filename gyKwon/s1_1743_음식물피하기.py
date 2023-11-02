import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 0
    while q:
        x,y = q.popleft()
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
                    cnt += 1
    return cnt

def wheres():
    cnt = -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                cnt = max(cnt,bfs(i,j))
    return cnt


N,M,K = map(int,input().split())
arr = [[0]*M for _ in range(N)]
visited = [[0]*M for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1

fin = wheres()

print(fin+1)
