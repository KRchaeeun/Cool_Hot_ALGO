from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0
    while q:
        i,j = q.popleft()
        for di,dj in ([1,0],[0,1],[-1,0],[0,-1]):
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m and not visited[ni][nj] and arr[ni][nj] == 'L':
                visited[ni][nj] = visited[i][j] + 1
                cnt = max(cnt,visited[ni][nj])
                q.append((ni,nj))
    return cnt

n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
fina = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            if fina < bfs(i,j):
                fina = bfs(i,j)

print(fina-1)
