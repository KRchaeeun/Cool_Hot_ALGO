import sys, heapq
input = sys.stdin.readline
def dijkstra():
    pq = []
    heapq.heappush(pq,(0,0,0))
    visited[0][0] = 0
    while pq:
        dist,i,j = heapq.heappop(pq)
        if visited[i][j] < dist:
            continue
        for di,dj in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<m and 0<=nj<n:
                if visited[ni][nj]> dist + arr[ni][nj]:
                    visited[ni][nj] = dist + arr[ni][nj]
                    heapq.heappush(pq, (visited[ni][nj], ni, nj))


n, m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(m)]
INF = int(10e9)
visited = [[INF]*n for _ in range(m)]
dijkstra()
print(visited[m-1][n-1])
