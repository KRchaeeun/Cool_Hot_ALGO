import sys
sys.setrecursionlimit(10**6)


n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
max_cnt = 0
visited = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def dfs(i, j):
    global cnt
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] == 1 and not visited[ni][nj]:
                visited[ni][nj] = 1
                cnt += 1
                dfs(ni, nj)



for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            max_cnt = max(max_cnt, cnt)

print(max_cnt)