from collections import deque
import sys
input = sys.stdin.readline
def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i,j = q.popleft()
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<m and 0<=nj<n and not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
                cnt += 1
                visited[ni][nj] = 1
                q.append((ni,nj))
    return cnt


n,m = map(int,input().split())
arr = [list(input()) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
our = 0
oppo = 0

for i in range(m):
    for j in range(n):
        if arr[i][j] == 'W' and not visited[i][j]:
            our += (bfs(i,j))**2

        elif arr[i][j] == 'B' and not visited[i][j]:
            oppo += (bfs(i,j))**2


print(our, oppo)




